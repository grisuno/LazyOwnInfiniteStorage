import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from lazy_infinitestorage import encode_file_to_video, decode_video_to_file

class EncodeDecodeForm(FlaskForm):
    input_string = StringField('Input File Path', validators=[DataRequired()])
    output_string = StringField('Output File Path', validators=[DataRequired()])
    width = IntegerField('Frame Width', validators=[DataRequired()])
    height = IntegerField('Frame Height', validators=[DataRequired()])
    fps = IntegerField('Frames Per Second', validators=[DataRequired()])
    block_size = IntegerField('Block Size', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_REFRESH_EACH_REQUEST'] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EncodeDecodeForm()
    result = None
    action = None
    if form.validate_on_submit():
        input_file = secure_filename(form.input_string.data)
        output_file = secure_filename(form.output_string.data)
        width = form.width.data
        height = form.height.data
        fps = form.fps.data
        block_size = form.block_size.data
        action = request.form.get('action')

        try:
            if action == 'encode':
                encode_file_to_video(input_file, output_file, (width, height), fps, block_size)
                result = f"File encoded successfully to {output_file}"
            elif action == 'decode':
                decode_video_to_file(input_file, output_file, block_size)
                result = f"File decoded successfully to {output_file}"
            flash('Operation successful!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')

    return render_template('index.html', form=form, result=result, action=action)

@app.after_request
def add_security_headers(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# Uncomment the following lines if you want to run the app locally without Gunicorn
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
