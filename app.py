import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ishan/Desktop/Dev/solr_project/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    return render_template("file_upload.html") 
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(url_for('error'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return redirect(url_for('error'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("acknowledgement.html", name = filename)  
        
@app.route('/error')  
def error():  
    return "<h1>File not found</h1>"
