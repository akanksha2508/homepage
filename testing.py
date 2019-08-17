#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:27:10 2019

@author: newuser
"""


def testing(test_feature):
    import pickle
    from keras.models import Sequential
    from keras.layers import Dense
    from sklearn.datasets.samples_generator import make_blobs
    from sklearn.preprocessing import MinMaxScaler
    
    Xnew=test_feature.reshape(test_feature.shape[0], (test_feature.shape[1]* 
                              test_feature.shape[2]*test_feature.shape[3]))
    newModel = pickle.loads(saved_model) 
    
# make a prediction
    ynew = newModel.predict_classes(Xnew)
    return ynew
   
    
    

      
    
    

    