import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from db import db

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)

from model import Movie

with app.app_context():
    db.create_all()


@app.route("/")
def main():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)

@app.route("/upload")
@app.route("/upload/<sucess>")
def upload(sucess=None):
    return render_template("upload.html", sucess=sucess)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/uploadfile", methods=['GET', 'POST'])
def uploadFile():
    print(request.form['titleInput'])
    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect("/upload")
    #     file = request.files['file']
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         return redirect(url_for('download_file', name=filename))

    # newMovie = Movie(
    #     title=request.form['titleInput'],
    #     director=request.form['directorInput'],
    #     genres=request.form['genresInput'],
    #     # get run time: run_time = 
    #     poster=request.files.to_dict.keys()[1],
    #     link=request.files.to_dict.keys()[0]
    # )
    # db.session.add(newMovie)
    # db.session.commit()

    return redirect(url_for('upload', sucess=(request.form['titleInput']!="")))
        



if __name__ == "__main__":
    app.run(debug=True)