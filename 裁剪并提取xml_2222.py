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
 
ImgPath = 'D:/data/plate_img/'
AnnoPath = 'D:/data/plate_xml3/'

newImgPath = 'D:/data/newimg/'
newAnnPath = 'D:/data/newxml/'

ImgPath2 = 'D:/data/vel_img/'
AnnoPath2 = 'D:/data/vel_xml3/'

 
if not os.path.exists(newImgPath):
    os.makedirs(newImgPath)
if not os.path.exists(newAnnPath):
    os.makedirs(newAnnPath)

imagelist = os.listdir(ImgPath)
imagelist2 = os.listdir(ImgPath2)



for image in imagelist:
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image 
    xmlfile = AnnoPath + image_pre + '.xml'
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    file = root.find('filename')

    #print(file)
       
    logo_boxes = []
    veh_boxes = []
    
    for object in root.findall('object'):
        objectname = object.find('name').text
        bndbox = object.find('bndbox')
        xmin_logo = int(bndbox.find('xmin').text)
        xmax_logo = int(bndbox.find('xmax').text)
        ymin_logo = int(bndbox.find('ymin').text)
        ymax_logo = int(bndbox.find('ymax').text)
        logo_boxes.append((xmin_logo,ymin_logo,xmax_logo,ymax_logo,objectname))
        for image2 in imagelist2:
        
            image_pre2, ext2 = os.path.splitext(image2)
            imgfile2 = ImgPath2 + image2
            xmlfile2 = AnnoPath2 + image_pre2 + '.xml'

            tree2 = ET.parse(xmlfile2)
            root2 = tree2.getroot()
    
            file2 = root2.find('filename')    
    
    
            for object2 in root2.findall('object'):
                bndbox2 = object.find('bndbox')
                xmin_veh = int(bndbox2.find('xmin').text)
                xmax_veh = int(bndbox2.find('xmax').text)
                ymin_veh = int(bndbox2.find('ymin').text)
                ymax_veh = int(bndbox2.find('ymax').text)
                w = xmax_veh - xmin_veh
                h = ymax_veh - ymin_veh
                veh_boxes.append((xmin_veh,ymin_veh,xmax_veh,ymax_veh,w,h))
        
                #print(xmin_veh,xmin_logo)
                if image ==image2:
                    #if((xmin_logo>xmin_veh)):
                    xmin_logo_new = xmin_logo - xmin_veh
                    ymin_logo_new = ymin_logo - ymin_veh
                    xmax_logo_new = xmax_logo - xmin_veh
                    ymax_logo_new = ymax_logo - ymin_veh
                    
                    img = Image.open(imgfile2)
                    cropimg = img.crop((xmin_veh,ymin_veh,xmax_veh,ymax_veh))
                    saveimgpath = newImgPath + image_pre2 + '.jpg'
                    savexmlpath = newAnnPath + image_pre2 + '.xml'
                    cropimg.save(saveimgpath)
                    
                    root2 = ET.Element('Annotation')
                    ET.SubElement(root, 'filename').text = image_pre2 + '.jpg'
                    sizes = ET.SubElement(root2,'size')
                    ET.SubElement(sizes, 'width').text =str(w)
                    ET.SubElement(sizes, 'height').text =str(h)
                    ET.SubElement(sizes, 'depth').text = '3'
                    objects = ET.SubElement(root2, 'object')
                    ET.SubElement(objects, 'name').text = 'plate'
                    ET.SubElement(objects, 'pose').text = 'Unspecified'
                    ET.SubElement(objects, 'truncated').text = '0'
                    ET.SubElement(objects, 'difficult').text = '0'
                    bndbox2 = ET.SubElement(objects,'bndbox')
                    ET.SubElement(bndbox2, 'xmin').text = str(xmin_logo_new)
                    ET.SubElement(bndbox2, 'ymin').text = str(ymin_logo_new)
                    ET.SubElement(bndbox2, 'xmax').text = str(xmax_logo_new)
                    ET.SubElement(bndbox2, 'ymax').text = str(ymax_logo_new)
                    tree = ET.ElementTree(root2)
                    tree.write(savexmlpath, encoding='utf-8')
print ('\n processed done!!!!!')