#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:29:17 2019

@author: newuser
"""

import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("DATASET/NON_SWITCH/sofa/"): 
        dst ="sofa" + str(i) + ".jpg"
        src ='DATASET/NON_SWITCH/sofa/'+ filename 
        dst ='DATASET/NON_SWITCH/sofa/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 