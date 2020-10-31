# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:51:12 2019

@author: A
"""
from __future__ import division
import os
from PIL import Image

savepath = 'E:/export2/crop/'
 
if not os.path.exists(savepath):
    os.makedirs(savepath)
 
#temp_image_list=imagelist[24888]

f2 = open("E:/export2/vehicle.txt","r")

lines1 = f2.readlines()

i = 1   
for line1 in lines1:
    li1  = line1.strip().split(',')
    #print(li[1],li[4],li[5],li[6],li[7])
    file1 = li1[0]
    x1 = int(float(li1[1]))
    y1 = int(float(li1[2]))
    x2 = int(float(li1[3])+float(li1[1]))
    y2 = int(float(li1[4])+float(li1[2]))
        
    objectname =str(li1[5])
    
    imgfile = 'G:/shipin2/' + file1
    img = Image.open(imgfile)
        
    
    cropbox = (x1,y1,x2,y2)
    cropedimg = img.crop(cropbox)
        
    image_save1=savepath+objectname
    if not os.path.exists(image_save1):
        os.makedirs(image_save1)
    single_save2=image_save1 +'/'+ str(file1)[-4]+ '_'+ format(str(i),'0>4s') + '.jpg'
    cropedimg.save(single_save2,'jpeg')               

    i += 1
    print ("totally " + str(i) + " images processed")

print ('\n processed done!!!!!')