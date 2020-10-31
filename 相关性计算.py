# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:12:46 2019

@author: A
"""

import scipy.stats as stats

f1 = open("D:/Code/vehicel_plate/plate_label2.txt","r",encoding='utf-8-sig')
f2 = open("D:/Code/vehicel_plate/plate_hyperlpr_gru_wan.txt","r",encoding='utf-8-sig')
f3 = open("D:/Code/vehicel_plate/plate_hyperlpr_wan.txt","r",encoding='utf-8-sig')


#out = open("D:/Code/vehicel_plate/error_yolo_gru.txt","a",encoding='utf-8')
lines = f1.readlines()
lines2 = f2.readlines()
lines3 = f3.readlines()


tong1 = []
tong2 = []
tong3 = []

for line in lines:
    
    li  = line.strip().split(',')
    filename1 = li[0]
    plate1 = li[1]
    label1 = filename1+','+plate1
    tong1.append(plate1)


for line2 in lines2:
    li2  = line2.strip().split(',')
    filename2 = li2[0]
    plate2 = li2[1]
    label2 = filename2+','+plate2
    tong2.append(plate2)
    
for line3 in lines3:
    li3  = line3.strip().split(',')
    filename3 = li3[0]
    plate3 = li3[1]
    label3 = filename3+','+plate3
    tong3.append(plate3)
#求交集的两种方式        
list1 = []
list2 = []
for i in tong1:
    if i in tong2:
        list1.append(1)
    if i not in tong2:
        list1.append(0)
for j in tong1:
    if j in tong3:
        list2.append(1)
    if j not in tong3:
        list2.append(0)
        
print(list1)
print(list2)

xiang = stats.pearsonr(list1,list2)
print(xiang)


