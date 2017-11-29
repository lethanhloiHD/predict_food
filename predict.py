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
img = image.load_img('food/test/pho.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x /=255.0

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
pred = model.predict(images)
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['data']:
        if(classes == p['code']):
            print('Name: ' + p['name'])
            print ( pred )

#
# from keras.models import load_model
# from keras.preprocessing import image
# import matplotlib.pyplot as plt
# import numpy as np
# import json
#
# img_width, img_height = 96, 96
# def load_image(img_path):
#
#     img = image.load_img(img_path, target_size=(img_width, img_width))
#     img_tensor = image.img_to_array(img)                    # (height, width, channels)
#     img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
#     img_tensor /= 255.0                                      # imshow expects values in the range [0, 1]
#     return img_tensor
#
#
# if __name__ == "__main__":
#
#     # load model
#     model = load_model('models/models.h5')
#
#     # image path
#     img_path = 'food/test/pho.jpg'
#
#     # load a single image
#     new_image = load_image(img_path)
#
#     # check prediction
#     pred = model.predict(new_image)
#     classes = model.predict_classes(new_image, batch_size=10)
#     with open('data.txt') as json_file:
#         data = json.load(json_file)
#         for p in data['data']:
#             if(classes == p['code']):
#                 print('Name: ' + p['name'])
#
#     print (pred)