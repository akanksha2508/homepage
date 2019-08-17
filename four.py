#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:22:31 2019

@author: newuser
"""

import cv2
import os
import natsort
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import pickle 
from feature_extraction import feature_extraction
from testing import testing
from gtts import gTTS 
# load the model
model = VGG16(weights='imagenet', include_top=False)
cwd = os.getcwd()
swithRunDir=cwd +str('/DATASET/SWITCH/')  
nonswithRunDir=cwd +str('/DATASET/NON_SWITCH/')  

#grayFrameList = [ ]
switch_vggFeature=[]
nonswitch_vggFeature=[]
##########################################################
# Read frames from a folder
sortRunDir=natsort.natsorted(os.listdir(swithRunDir),reverse=False)
for file in sortRunDir:
    path=os.path.join(swithRunDir,file)
   # image = cv2.imread(path, 1)
    img = load_img(path, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    
    # VGG feature compute
    vggFeature = model.predict(img)
    switch_vggFeature.append(vggFeature)
#----------------------------------------------------------
sortRunDir2=natsort.natsorted(os.listdir(nonswithRunDir),reverse=False)
for file in sortRunDir2:
    path=os.path.join(nonswithRunDir,file)
   # image = cv2.imread(path, 1)
    img = load_img(path, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    
    # VGG feature compute
    vggFeature = model.predict(img)
    nonswitch_vggFeature.append(vggFeature)
      
###############################################################
#Data preprocessing
switch_vggFeature= np.asarray(switch_vggFeature)
nonswitch_vggFeature= np.asarray(nonswitch_vggFeature)  

switch_data=switch_vggFeature.reshape(switch_vggFeature.shape[0], (switch_vggFeature.shape[2]* switch_vggFeature.shape[3]*switch_vggFeature.shape[4]))
nonswitch_data=nonswitch_vggFeature.reshape(nonswitch_vggFeature.shape[0], (nonswitch_vggFeature.shape[2]* nonswitch_vggFeature.shape[3]*nonswitch_vggFeature.shape[4]))

switchLabel=np.ones(switch_data.shape[0])
nonswitchLabel=np.zeros(nonswitch_data.shape[0])

X=np.concatenate((switch_data,nonswitch_data)) 
Y=np.concatenate((switchLabel,nonswitchLabel)) 

X, Y = shuffle(X, Y, random_state=0)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

###############################################################
# Train own model
myModel = Sequential()
myModel.add(Dense(12, input_dim=25088, activation='relu'))
myModel.add(Dense(8, activation='relu'))
myModel.add(Dense(1, activation='sigmoid'))
#print(myModel.summary())
# Compile model
myModel.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
myModel.fit(X_train, Y_train, epochs=10, batch_size=128)
# evaluate the model
scores = myModel.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (myModel.metrics_names[1], scores[1]*100))


saved_model = pickle.dumps(myModel) 

############################

# load an imagetfeature on image

# call feature_extraction
test_feature=feature_extraction(cwd+str('/DATASET/NON_SWITCH/chair1.jpg'))
# call testing fxn on extracted feature

ynew = testing(test_feature)

language = 'en'

if ynew==1:
    mytext="IT IS A SWITCH"
else:
    mytext="IT IS NOT A SWITCH"
    
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("result.mp3") 
  
# Playing the converted file 
os.system("mpg321 result.mp3") 



