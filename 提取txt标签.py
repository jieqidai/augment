# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:37:19 2019

@author: A
"""

import os

path = 'D:/Code/vehicel_plate/yolov3-master/data/test_wanshang'
images = os.listdir(path)

f1 = open("H:/数据集/打逃数据/jietu/京珠北卡口2016年数据1/京珠北卡口2016年数据1分析结果_plate/images10_plate_total.txt","r",encoding='utf-8-sig')
lines = f1.readlines()

out = open("D:/Code/vehicel_plate/gaokaowan3.txt","w",encoding='utf-8')

for image in images:
    name = image
    for line in lines:
        line =line.strip().split(',')
        filename = line[0]
        if name == filename:
            out.writelines(line[0]+','+line[-2]+'\n')
out.close()
    