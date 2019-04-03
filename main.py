import predict, diagnose
import os
from flask import render_template, Flask, request, flash, redirect, url_for
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PROJECT_ID = "bionic-water-236108"
DATA_ID = "ICN7305758534645962463"

@app.context_processor
def data_processor():
    return dict(getdata=diagnose.get_data)


def prediction(filepath):
    with open(filepath, 'rb') as ff:
        content = ff.read()
    return predict.get_prediction(content, PROJECT_ID, DATA_ID)


@app.route('/')
def hello_world():
    # labels = prediction('./static/uploads/panda1.jpg').payload
    # predict.get_prediction('./static/uploads/panda1.jpg', PROJECT_ID, DATA_ID)
    return render_template('test.html', currimg="static/uploads/itchyarmpit.png")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
            hello_world()
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # rdr =
            redirect(url_for('upload_file', filename=filename))
            # filepath = UPLOAD_FOLDER + '/' + filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            labels = prediction(filepath).payload
            labelinfo = diagnose.get_data(labels[0].display_name)
            # print(labels)
            return render_template('test.html', currimg=filepath, labels=labels, info=labelinfo)
            # return rdr
    # hello_world()
    return 0


if __name__ == "__main__":
    app.run()
