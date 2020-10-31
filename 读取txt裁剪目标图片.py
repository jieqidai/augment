# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:51:12 2019

@author: A
"""
from __future__ import division
from PIL import Image
import os


import xml.dom.minidom
from xml.dom.minidom import Document
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree,Element
import numpy as np

def label2picture(cropimg,name):
    pathnew ="D:\\Code\\vehicel_plate\\vel_crop\\"
    # cv2.imshow("image", cropImg)
    # cv2.waitKey(1)
    
    if (os.path.exists(pathnew)):
        cropimg.save(pathnew +'\\'+ name[:-4]+'_'+format(str(i),'0>4s')+'.jpg')
        
 
    else:
        os.makedirs(pathnew)
        cropimg.save(pathnew +'\\'+ name[:-4]+'_'+format(str(i),'0>4s')+'.jpg')
 
f1 = open("D:/Code/vehicel_plate/plate-2.txt","r")
f2 = open("D:/Code/vehicel_plate/vehicle-2.txt","r")
lines1 = f1.readlines()
lines2 = f2.readlines()
i=0
for line1 in lines1:
    li1  = line1.split(',')
    #print(li[1],li[4],li[5],li[6],li[7])
    file1 = li1[0]
    xmin1 = int(float(li1[1]))
    ymin1 = int(float(li1[2]))
    xmax1 = int(float(li1[3])+float(li1[1]))
    ymax1 = int(float(li1[4])+float(li1[2]))
    
    for line2 in lines2:
        li2  = line2.split(',')
        file2 = li2[0]
        xmin2 = int(float(li2[1]))
        ymin2 = int(float(li2[2]))
        xmax2 = int(float(li2[3])+float(li2[1]))
        ymax2 = int(float(li2[4])+float(li2[2]))
    
        if file1 == file2:
            if xmin2<xmin1 and ymin2<ymin1 and ymax2>ymax1 and xmax2>xmax1:
                xmin = xmin1-xmin2
                ymin = ymin1-ymin2
                xmax = xmax1-xmin2
                ymax = ymax1-ymin2
            
                w = xmax2-xmin2
                h = ymax2-ymin2
    
    
    #name = li[2]
    #if name[0:1] !='粤':
                filename = file1
                pathnew ="D:\\Code\\vehicel_plate\\vel_crop\\"
                imgfile = "D:/data/plate_img/" + filename
                try:
                    img = Image.open(imgfile)
                except:
                    continue
        #print(img)

                cropimg = img.crop((xmin2,ymin2,xmax2,ymax2))

    # print(int(li[2][:-3]),int(li[3][:-3]),int(li[4][:-3]),int(li[5][:-3]))
                label2picture(cropimg, filename)
            
                savexmlpath = pathnew +'\\'+ filename[:-4]+'_'+format(str(i),'0>4s') + '.xml'
            
                    
                root = ET.Element('Annotation')
                ET.SubElement(root, 'filename').text = filename[:-4]+'_'+format(str(i),'0>4s')+'.jpg'
                sizes = ET.SubElement(root,'size')
                ET.SubElement(sizes, 'width').text =str(w)
                ET.SubElement(sizes, 'height').text =str(h)
                ET.SubElement(sizes, 'depth').text = '3'
                objects = ET.SubElement(root, 'object')
                ET.SubElement(objects, 'name').text = 'plate'
                ET.SubElement(objects, 'pose').text = 'Unspecified'
                ET.SubElement(objects, 'truncated').text = '0'
                ET.SubElement(objects, 'difficult').text = '0'
                bndbox = ET.SubElement(objects,'bndbox')
                ET.SubElement(bndbox, 'xmin').text = str(xmin)
                ET.SubElement(bndbox, 'ymin').text = str(ymin)
                ET.SubElement(bndbox, 'xmax').text = str(xmax)
                ET.SubElement(bndbox, 'ymax').text = str(ymax)
                tree = ET.ElementTree(root)
                tree.write(savexmlpath, encoding='utf-8')
    i+=1
# #
# x,y,w,h = 87,158,109,222
# img = cv2.imread("E:\\DeeCamp\\img1\\1606.jpg")
# # print(img.shape)
# crop = img[y:(h+y),x:(w+x)]
# cv2.imshow("image", crop)
# cv2.waitKey(0)
# img = Image.open("E:\\DeeCamp\\img1\\3217.jpg")
#
# cropImg = img.crop((x,y,x+w,y+h))
# cropImg.show()
    # img = Image.open("E:\\deep_sort-master\\MOT16\\train\\try1\\img1\\"+filename)
    # print(int(li[2][:-3]),(int(li[2][:-3])+int(li[4][:-3])), int(li[3][:-3]),(int(li[3][:-3])+int(li[5][:-3])))
 
    # #裁切图片
    # # cropImg = img.crop(region)
    # # cropImg.show()
    # framenum ,tracker= li[0],li[1]
    # pathnew = 'E:\\DeeCamp\\deecamp项目\\deep_sort-master\\crop_picture\\'
    # if (os.path.exists(pathnew + tracker)):
    #     # 保存裁切后的图片
    #     plt.imshow(cropImg)
    #     plt.savefig(pathnew + tracker+'\\'+framenum + '.jpg')
    # else:
    #     os.makedirs(pathnew + tracker)
    #     plt.imshow(cropImg)
    #     plt.savefig(pathnew + tracker+'\\'+framenum + '.jpg')