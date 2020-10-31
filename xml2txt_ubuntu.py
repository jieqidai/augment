# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:32:09 2019

@author: A
"""

# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = []
'''
classes = ['Alpina','Aston Martin', 'AK', 'Audi', 'Baojun','BMW', 'Borgward', 'Porsche', 'Beiben', 'North',
           'Beiqi', 'Benz', 'Honda', 'BYD', 'PEUGEOT', 'Buick', 'Bentley', 'Changhe', 'Chenglong', 'MAXUS',
           'Daewoo', 'Dayun', 'Volkswagen', 'Daoda', 'Dodge', 'DS', 'AEOLUS', 'Venucia', 'Ferrari', 'FIAT',
           'Toyota', 'X', 'Keyton', 'Ford', 'Mustang', 'FOTON', 'Forland', 'QOROS', 'Trumpchi', 'Hafei',
           'Haval', 'Higer', 'Haima', 'Hanteng', 'Hummer', 'HOWO', 'Constant day', 'Hongqi', 'Huakai', 'CAMC',
           'Huapu', 'Horki', 'Huasong', 'GONOW', 'Geely', 'GMC', 'Jeep', 'JAC', 'JMC', 'Yusheng',
           'Jaguar', 'Jinbei', 'King long', 'Jolden dragon','Jiulong', 'Traum', 'Carlsson', 'Kawei', 'Karry', 'Cadillac',
           'Kama', 'Cowin', 'Kandi', 'Koenigsegg', 'Chrysler', 'Lamborghini', 'Rolls-Royce', 'Lexus', 'Renault', 'EVERUS',
           'Lelifan', 'U', 'Leopaard', 'Lincoln', 'Suzuki', 'GreenWheel', 'Lufeng', 'Landrover', 'Lotus', 'Mazda',
           'Maserati', 'Maybach', 'McLaren', 'Man', 'Mini', 'MG', 'Morgan', 'Luxgen', 'Naveco', 'Acura',
           'Opel', 'Pagani', 'Chery', 'KIA', 'Qiantu', 'Youngman', 'Youngmanlotus', 'Nissan', 'UD', 'Hino',
           'Roewe', 'Ruf', 'Riich', 'Scion', 'Mitsubishi', 'Shanqi', 'SHAC', 'Shaolin', 'Sunlong', 'Spyker',
           'Shuanghuan', 'SsangYong', 'Subaru', 'Scania', 'Skoda', 'Smart', 'SWM', 'Techart', 'Tesla', 'Denza',
           'Rely', 'Wiesmann', 'Enranger', 'NIO', 'Volvo', 'SGMW', 'ISUZU', 'SSC', 'Seat', 'Hyundai',
           'Xpeng', 'Xinkai', 'Chevrolet', 'Citroen', 'Asiastar', 'Ycaco', 'Yema', 'Yiqi', 'Iveco', 'Infiniti', 
           'Jonway', 'Youxia', 'Yutong', 'Yuejin', 'CHANGNA', 'Jinniuxing', 'Oushang', 'Greatwall', 'Zinoro', 'Know beans',
           'Brilliance', 'Zhongtong', 'ZX-auto', 'Zotye','Fudi', 'Hongyan','Xugong', 'WEY','Wuzhoulong','Soueast',
           'Huatai','Huanghai','CIIMO','Xiali','Englon','Weiwang','Yuxuan','Wangpai','Benteng','Nanjun',
           'Shifeng','Shuchi','Junwei','Suitong','Xindadi','NEOPLAN','Steyr','Marcopolo','Tangjun','Zhidao', 
           'other']
'''
classes = ['vehicle']

#原样保留。size为图片大小
# 将ROI的坐标转换为yolo需要的坐标
# size是图片的w和h
# box里保存的是ROI的坐标（x，y的最大值和最小值）
# 返回值为ROI中心点相对于图片大小的比例坐标，和ROI的w、h相对于图片大小的比例
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])

    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert2(size, box):
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]

    return (x1,y1,x2,y2)


def convert_annotation(image_add):
    #image_add进来的是带地址的.jpg
    image_add = os.path.split(image_add)[1] #截取文件名带后缀
    image_add = image_add[0:image_add.find('.',1)] #删除后缀，现在只有文件名没有后缀
    print(image_add)
    #现在传进来的只有图片名没有后缀
   
    in_file = open('E:/export/xml/' + image_add + '.xml')
    
    out_file = open('E:/export/txt/%s.txt'%(image_add), 'w')
    #out_file = open('E:/export/train.txt', 'a')

    tree=ET.parse(in_file)
    root = tree.getroot()


    size = root.find('size')
    
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    #在一个XML中每个Object的迭代
    for obj in root.iter('object'):
        #iter()方法可以递归遍历元素/树的所有子元素
    
        difficult = obj.find('difficult').text
        #找到所有的椅子
        cls = obj.find('name').text
        #如果训练标签中的品种不在程序预定品种，或者difficult = 1，跳过此object
        if cls not in classes or int(difficult)==1:
            continue
        #cls_id 只等于1
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        #b是每个Object中，一个bndbox上下左右像素的元组
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + "," + ",".join([str(a) for a in bb]) + '\n')


if not os.path.exists('E:/export/txt/'):
    os.makedirs('E:/export/txt/')
image_adds = open("E:/export/name.txt")
for image_add in image_adds:
    #print(image_add)
    image_add = image_add.strip()
    #print (image_add)
    convert_annotation(image_add)
