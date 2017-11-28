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
model.compile(optimizer=SGD(lr=0.001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])

# predicting images
img = image.load_img('food/test/pho2.jpg', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['data']:
        if(classes == p['code']):
            print('Name: ' + p['name'])


#
# from keras.models import load_model
# from keras.preprocessing import image
# import matplotlib.pyplot as plt
# import numpy as np
# import os
#
#
# def load_image(img_path, show=False):
#
#     img = image.load_img(img_path, target_size=(img_width, img_width))
#     img_tensor = image.img_to_array(img)                    # (height, width, channels)
#     img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
#     img_tensor /= 255.0                                      # imshow expects values in the range [0, 1]
#
#     if show:
#         plt.imshow(img_tensor[0])
#         plt.axis('off')
#         plt.show()
#
#     return img_tensor
#
#
# if __name__ == "__main__":
#
#     # load model
#     model = load_model('models/models.h5')
#
#     # image path
#     img_path = 'food/train1/pho/926.jpg'
#
#     # load a single image
#     new_image = load_image(img_path)
#
#     # check prediction
#     pred = model.predict(new_image)
#     print ( pred )