# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:30:26 2019

@author: Administrator
"""

# -*- coding:utf-8 -*-

from __future__ import print_function
import os, sys, zipfile
import numpy as np
import json

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[0] + box[2]) / 2.0
    y = (box[1] + box[1] + box[3]) / 2.0
    w = box[2]
    h = box[3]
    #x = (box[0] + box[1])/2.0 - 1
    #y = (box[2] + box[3])/2.0 - 1
    #w = box[1] - box[0]
    #h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


json_file='E:/code/annotations/instances_train2014.json' # # Object Instance 类型的标注


data=json.load(open(json_file,'r'))

ana_txt_save_path = "./train_cocoperson/"
if not os.path.exists(ana_txt_save_path):
    os.makedirs(ana_txt_save_path)

for img in data['images']:
    print(img["id"])
    #print(img["file_name"])
    filename = img["file_name"]
    img_width = img["width"]
    img_height = img["height"]
    #print(img["height"])
    #print(img["width"])
    img_id = img["id"]
    ana_txt_name = filename.split(".")[0] + ".txt"
    f_txt = open(os.path.join(ana_txt_save_path, ana_txt_name), 'w')
    for ann in data['annotations']:
        if ann['image_id']==img_id:
            #if ann['category_id'] >8 or ann['category_id']==2 or ann['category_id']==5 or ann['category_id']==7 or ann['category_id']==4:
            #    continue
            if ann['category_id'] ==1:   #person
                box = convert((img_width,img_height), ann["bbox"])
                f_txt.write("%s %s %s %s %s\n"%('0', box[0], box[1], box[2], box[3]))
            #if ann['category_id'] ==3:   #car
            #    box = convert((img_width,img_height), ann["bbox"])
            #    f_txt.write("%s %s %s %s %s\n"%('0', box[0], box[1], box[2], box[3]))
            #if ann['category_id'] ==4:   #motorcycle
            #    box = convert((img_width,img_height), ann["bbox"])
            #    f_txt.write("%s %s %s %s %s\n"%('2', box[0], box[1], box[2], box[3]))
            #if ann['category_id'] ==6:   #bus
            #    box = convert((img_width,img_height), ann["bbox"])
            #    f_txt.write("%s %s %s %s %s\n"%('0', box[0], box[1], box[2], box[3]))
            #if ann['category_id'] ==8:   #truck
            #    box = convert((img_width,img_height), ann["bbox"])
            #    f_txt.write("%s %s %s %s %s\n"%('0', box[0], box[1], box[2], box[3]))
        
            #else:        #others
                #continue
                #box = convert((img_width,img_height), ann["bbox"])
                #f_txt.write("%s %s %s %s %s\n"%('2', box[0], box[1], box[2], box[3]))
            
    f_txt.close()
    
    
    