from keras.models import load_model
from keras.preprocessing import image

import numpy as np
import json
from keras.optimizers import Adam , SGD

# dimensions of our images
img_width, img_height = 96, 96
#
# load the model we saved
model = load_model('models/models.h5')
# model.compile(optimizer=SGD(lr=0.001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])

# predicting images
img = image.load_img('food/test/hotdog1.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x /=255.0

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
pred = model.predict(images)
with open('data.txt') as json_file:
    data = json.load(json_file)
    i=0
    for p in data['data']:
        print(p['id'])
        print(p['name'])
        print( pred[0][i]*100 )
        i +=1
        print("RESULT :")
        # if(classes == p['id']):
        #     print('id  : '+ str(p['id']))
        #     print('Name: ' + p['name'])

 
