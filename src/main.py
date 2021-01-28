import secrets
import os

from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'}
secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = secret


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def index():
    return render_template('index.html')


def show_video():
    return render_template('show_video.html', char=request.args.get('char'))


# @app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        # filename = photos.save(request.files['photo'])
        # rec = Photo(filename=filename, user=g.user.id)
        # rec.store()
        flash("Photo saved.")
        print('photo saved')
        print(request.files)
        # return redirect(url_for('index', id=rec.id))
        return redirect(url_for('index'))
    return render_template('index.html')


def upload_file():
    if request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('text-to-speak'))
        print(request.form.get('img-select'))
        email = request.form.get('email')
        text_to_speak = request.form.get('text-to-speak')
        img = request.form.get('img-select')

        if email and text_to_speak and img:
            # Send the model request here
            return redirect(url_for('show_video', char=img))

    return render_template('index.html')


app.add_url_rule('/', 'index', index)
app.add_url_rule('/show-video', 'show_video', show_video, methods=['GET', 'POST'])
app.add_url_rule('/upload', 'upload', upload_file, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
