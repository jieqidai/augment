# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:51:12 2019

@author: A
"""
from __future__ import division
from PIL import Image

import xml.dom.minidom
from xml.dom.minidom import Document
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element
import numpy as np
import os


f2 = open("D:/data/export(1)/vehicle-2.txt","r")

lines2 = f2.readlines()

imgfile = 'H:/random_pic' 

for img in os.listdir(imgfile):
    im = Image.open((imgfile + '/' + img))
    w, h = im.size
    
    pathnew ="D:/data/export(1)/txt2"
                      
    savexmlpath = pathnew +'\\'+ img[:-4] + '.txt'

    for line1 in lines2:
        li1  = line1.split(',')
    #print(li[1],li[4],li[5],li[6],li[7])
        file1 = li1[0]
        if img==file1:  
            xmin = float(li1[1])
            ymin = float(li1[2])
            xmax = float(li1[3])+float(li1[1])
            ymax = float(li1[4])+float(li1[2])

            with open(savexmlpath,'a') as f:
                f.writelines(str(xmin)+','+str(ymin)+','+str(xmax)+','+str(ymax)+',vehicle\n')
            #pathnew ="D:/data/export(1)/xml"
                      
            #savexmlpath = pathnew +'\\'+ filename[:-4] + '.xml'
            
                    
            #root = ET.Element('Annotation')
            #ET.SubElement(root, 'filename').text = filename
            #sizes = ET.SubElement(root,'size')
           # ET.SubElement(sizes, 'width').text =str(w)
           # ET.SubElement(sizes, 'height').text =str(h)
           # ET.SubElement(sizes, 'depth').text = '3'
           # print(img)
           # print(file1)
        
           # objects = ET.SubElement(root, 'object')
           # ET.SubElement(objects, 'name').text = 'vehicle'
           # ET.SubElement(objects, 'pose').text = 'Unspecified'
           # ET.SubElement(objects, 'truncated').text = '0'
           # ET.SubElement(objects, 'difficult').text = '0'
          #  bndbox = ET.SubElement(objects,'bndbox')
          #  ET.SubElement(bndbox, 'xmin').text = str(xmin)
          #  ET.SubElement(bndbox, 'ymin').text = str(ymin)
          #  ET.SubElement(bndbox, 'xmax').text = str(xmax)
          #  ET.SubElement(bndbox, 'ymax').text = str(ymax)
          #  tree = ET.ElementTree(root)
          #  tree.write(savexmlpath, encoding='utf-8')
  
