import os
import tempfile
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, jsonify, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from lazyown_infinitestorage import encode_file_to_video, decode_video_to_file

class EncodeDecodeForm(FlaskForm):
    input_file = FileField('Input File', validators=[DataRequired()])
    output_file_name = StringField('Output File Name', validators=[DataRequired()])
    frame_width = SelectField('Frame Width', choices=[('640', '640'), ('480', '480')])
    frame_height = SelectField('Frame Height', choices=[('480', '480'), ('360', '360')])
    block_size = SelectField('Block Size', choices=[('4', '4'), ('8', '8'), ('16', '16')])
    action = SelectField('Action', choices=[('encode', 'Encode'), ('decode', 'Decode')], validators=[DataRequired()])
    submit = SubmitField('Start')

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)

import os
import tempfile
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, jsonify, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from lazyown_infinitestorage import encode_file_to_video, decode_video_to_file

class EncodeDecodeForm(FlaskForm):
    input_file = FileField('Input File', validators=[DataRequired()])
    output_file_name = StringField('Output File Name', validators=[DataRequired()])
    frame_width = SelectField('Frame Width', choices=[('640', '640'), ('480', '480')])
    frame_height = SelectField('Frame Height', choices=[('480', '480'), ('360', '360')])
    block_size = SelectField('Block Size', choices=[('4', '4'), ('8', '8'), ('16', '16')])
    action = SelectField('Action', choices=[('encode', 'Encode'), ('decode', 'Decode')], validators=[DataRequired()])
    submit = SubmitField('Start')

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    result = None
    output_file_path = None

    if form.validate_on_submit():
        input_file = form.input_file.data
        output_file_name = secure_filename(form.output_file_name.data)
        frame_width = form.frame_width.data
        frame_height = form.frame_height.data
        block_size = form.block_size.data
        action = form.action.data

        input_file_path = os.path.join(tempfile.gettempdir(), secure_filename(input_file.filename))
        input_file.save(input_file_path)

        try:
            if action == 'encode':
                output_file_path = os.path.join(tempfile.gettempdir(), f"{output_file_name}_{frame_width}x{frame_height}.mp4")
                encode_file_to_video(input_file_path, output_file_path, (int(frame_width), int(frame_height)), 30, int(block_size))
            elif action == 'decode':
                output_file_path = os.path.join(tempfile.gettempdir(), f"{output_file_name}.zip")
                decode_video_to_file(input_file_path, output_file_path, int(block_size))
            flash('Operation successful!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
        finally:
            os.remove(input_file_path)

    return render_template('index.html', form=form, result=result, output_file_path=output_file_path)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        flash(f"File {filename} not found", 'danger')
        return redirect(url_for('index'))

@app.after_request
def add_security_headers(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
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
        output_filename = f'output_{frame_width}x{frame_height}.mp4'
        output_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
        encode_file_to_video(filepath, output_filepath, block_size, frame_width, frame_height)
    else:
        output_filename = 'output.zip'
        output_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
        decode_video_to_file(filepath, output_filepath)
    
    os.remove(filepath)
    download_url = f"/download/{output_filename}"
    
    return jsonify({'download_url': download_url})

# Uncomment the following lines if you want to run the app locally without Gunicorn
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

