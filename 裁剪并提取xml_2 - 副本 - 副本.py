# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:18:15 2019

@author: A
"""

from __future__ import division
import os
from PIL import Image
import xml.dom.minidom
from xml.dom.minidom import Document
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element
import numpy as np
 
ImgPath = 'F:/data/车标数据/logo_img/'
AnnoPath = 'F:/data/车标数据/logo_xml/'
#newImgPath = 'F:/data/车标数据/newimg/'
newAnnPath = 'F:/data/车标数据/velxml/'
 
#if not os.path.exists(newImgPath):
#    os.makedirs(newImgPath)
if not os.path.exists(newAnnPath):
    os.makedirs(newAnnPath)

imagelist = os.listdir(ImgPath)
for image in imagelist:
    print(image)
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image 
    xmlfile = AnnoPath + image_pre + '.xml'
    
    veh_boxes = []
    
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for object in root.findall('object'):
        objectname = object.find('name').text
        
        if objectname == 'vehicle':
            bndbox = object.find('bndbox')
            xmin_veh = int(bndbox.find('xmin').text)
            xmax_veh = int(bndbox.find('xmax').text)
            ymin_veh = int(bndbox.find('ymin').text)
            ymax_veh = int(bndbox.find('ymax').text)
 
            veh_boxes.append((xmin_veh,ymin_veh,xmax_veh,ymax_veh))
    print(veh_boxes)
    for i in range(0,len(veh_boxes)):
        xmin_veh = veh_boxes[i][0]
        ymin_veh = veh_boxes[i][1]
        xmax_veh = veh_boxes[i][2]
        ymax_veh = veh_boxes[i][3]

        #print(width)
        img = Image.open(imgfile)
        w, h = img.size[0],img.size[1]
        #cropimg = img.crop((xmin_veh,ymin_veh,xmax_veh,ymax_veh))
        #saveimgpath = newImgPath + image_pre + '-' + str(i) + '.jpg'
        savexmlpath = newAnnPath + image_pre +'.xml'
        #cropimg.save(saveimgpath)
        
        root = ET.Element('Annotation')
        ET.SubElement(root, 'filename').text = image_pre + '.jpg'
        sizes = ET.SubElement(root,'size')
        ET.SubElement(sizes, 'width').text =str(w)
        ET.SubElement(sizes, 'height').text =str(h)
        ET.SubElement(sizes, 'depth').text = '3'
        objects = ET.SubElement(root, 'object')
        ET.SubElement(objects, 'name').text = 'vehicle'
        ET.SubElement(objects, 'pose').text = 'Unspecified'
        ET.SubElement(objects, 'truncated').text = '0'
        ET.SubElement(objects, 'difficult').text = '0'
        bndbox = ET.SubElement(objects,'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(xmin_veh)
        ET.SubElement(bndbox, 'ymin').text = str(ymin_veh)
        ET.SubElement(bndbox, 'xmax').text = str(xmax_veh)
        ET.SubElement(bndbox, 'ymax').text = str(ymax_veh)
        tree = ET.ElementTree(root)
        tree.write(savexmlpath, encoding='utf-8')
print ('\n processed done!!!!!')