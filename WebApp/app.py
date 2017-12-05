import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from predict import predict

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    filename = 'static/pho.jpg'
    data = predict(filename)
    return render_template("index.html", image_name='pho.jpg', datas = data)

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    # for upload in request.files.getlist("file"):
    
    # print request.files.getlist("file")
    upload=request.files.getlist("file")[0]
    print "lol"
    print upload
    filename = upload.filename
    print filename
    destination = "/".join([target, filename])
    upload.save(destination)      
    print filename
    data = predict('images/'+filename)
    print 'data'
    print data
    return render_template("index.html",image_name=filename,datas=data)
    

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename=filename)