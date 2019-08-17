#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:27:28 2019

@author: newuser
"""
def feature_extraction(path):
    from keras.preprocessing.image import load_img
    from keras.preprocessing.image import img_to_array
    from keras.applications.vgg16 import preprocess_input
    from keras.applications.vgg16 import decode_predictions
    from keras.applications.vgg16 import VGG16

    model = VGG16(weights='imagenet', include_top=False)

    img = load_img(path, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    
    vggFeature = model.predict(img)
    return vggFeature 
