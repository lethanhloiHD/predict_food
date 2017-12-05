import os
from predict import predict

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    # for upload in request.files.getlist("file"):

    upload=request.files.getlist("file")[0]
    filename = upload.filename
    destination = "/".join([target, filename])
    upload.save(destination)      
    data = predict('images/'+filename)
    return render_template("index.html",image_name=filename,datas=data)
    

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename=filename)