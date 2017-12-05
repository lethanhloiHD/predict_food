from keras.models import load_model
from keras.preprocessing import image

import numpy as np
import json
from keras.optimizers import Adam , SGD


# result = {}
result=[]
# dimensions of our images
img_width, img_height = 96, 96
#
# load the model we saved
model = load_model('../models/models.h5')

# predicting images
def predict(path):
    result = []
    img = image.load_img(path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /=255.0

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)
    pred = model.predict(images)

    with open('../data.txt') as json_file:
        data = json.load(json_file)
        i=0
        for p in data['data']:
            result.append({
                    'id': p['id'],
                    'name': p['name'],
                    'acc' : pred[0][i]*100
                })
            i +=1
        for p in data['data']:
            if(p['id'] == classes):
                result.append({
                    'comment'
                    'id' : str(classes),
                    'name': p['name']
                })      
    return result

