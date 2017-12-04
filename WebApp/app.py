import numpy as np
import base64

from flask import Flask, request,render_template, make_response

app = Flask(__name__, static_url_path='/static')
# clf = joblib.load('clf.pkl')


@app.route('/')
def display_gui():
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        file_val = request.files['file']
        return file_val
    # data = request.get_json(silent=True)['image']
    # data = data[22:]

    # img = skio.imread(BytesIO(base64.b64decode(data)))[:,:,3]

    # img = make_mnist(img)

    # number = clf.predict(img.reshape(1, -1))[0]

