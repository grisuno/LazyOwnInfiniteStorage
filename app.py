import os
import re
import tempfile
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from lazyown_infinitestorage import encode_file_to_video, decode_video_to_file


class EncodeDecodeForm(FlaskForm):
    input_file = FileField('Input File', validators=[DataRequired()])
    output_file_name = StringField('Output File Name', validators=[DataRequired()])
    frame_width = IntegerField('Frame Width', validators=[DataRequired()])
    frame_height = IntegerField('Frame Height', validators=[DataRequired()])
    fps = IntegerField('Frames Per Second', validators=[DataRequired(), NumberRange(min=1)])  # Agregado el campo fps
    block_size = IntegerField('Block Size', validators=[DataRequired()])
    action = SelectField('Action', choices=[('encode', 'Encode'), ('decode', 'Decode')], validators=[DataRequired()])
    submit = SubmitField('Start')


def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '', filename)

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['UPLOAD_FOLDER'] = os.path.abspath(UPLOAD_FOLDER)
app.config['DOWNLOAD_FOLDER'] = os.path.abspath(DOWNLOAD_FOLDER)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['DOWNLOAD_FOLDER']):
    os.makedirs(app.config['DOWNLOAD_FOLDER'])

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    result = None
    output_file_path = None
    download_url = None

    if form.validate_on_submit():
        input_file = form.input_file.data
        output_file_name = secure_filename(sanitize_filename(form.output_file_name.data))
        frame_width = int(form.frame_width.data)
        frame_height = int(form.frame_height.data)
        block_size = int(form.block_size.data)
        action = form.action.data
        fps = int(form.fps.data)
        input_file_path = os.path.join(tempfile.gettempdir(), secure_filename(input_file.filename))
        input_file.save(input_file_path)

        try:
            if action == 'encode':
                output_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], f"{output_file_name}_{frame_width}x{frame_height}.mp4")
                encode_file_to_video(input_file_path, output_file_path, (frame_width, frame_height), fps, block_size)
                result = f"File encoded successfully to {output_file}"
            elif action == 'decode':
                output_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], f"{output_file_name}.zip")
                decode_video_to_file(input_file_path, output_file_path, block_size)
                result = f"File decoded successfully to {output_file}"
            flash('Operation successful!', 'success')
            download_url = url_for('download_file', filename=os.path.basename(output_file_path))
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
        finally:
            os.remove(input_file_path)

    return render_template('index.html', form=form, result=result, download_url=download_url)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    sanitized_filename = sanitize_filename(filename)
    sanitized_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], sanitized_filename)
    if os.path.exists(sanitized_file_path):
        return send_file(sanitized_file_path, as_attachment=True)
    else:
        flash(f"File {filename} not found", 'danger')
        return redirect(url_for('index'))

@app.after_request
def add_security_headers(response):
    # Configuración para evitar el almacenamiento en caché
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    # Configuración de protección adicional de seguridad
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    # Configuración de políticas de seguridad
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"

    return response


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    mode = request.form['mode']
    
    if mode == 'encode':
        block_size = int(request.form['block_size'])
        frame_width = int(request.form['frame_width'])
        frame_height = int(request.form['frame_height'])
        fps = int(request.form['frame_height'])
        output_filename = f'output_{frame_width}x{frame_height}.mp4'
        output_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
        download_url = url_for('download_file', filename=os.path.basename(output_file_path))
        encode_file_to_video(filepath, output_filepath, (frame_width, frame_height), fps, block_size)
    else:
        output_filename = 'output.zip'
        output_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
        decode_video_to_file(filepath, output_filepath, block_size)    
        download_url = url_for('download_file', filename=os.path.basename(output_file_path))

    os.remove(filepath)
    

    return render_template('index.html', form=form, result=result, action=action, download_url=download_url)


# Uncomment the following lines if you want to run the app locally without Gunicorn
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
