# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:31:24 2019

@author: A
"""

import cv2

def getImageVar(imgPath):
    image = cv2.imread(imgPath)
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    return imageVar

imageVar = getImageVar('C:/Users/A/Desktop/car/car/000001.jpg')
print(imageVar)