# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:13:13 2019

@author: A
"""
out1 = open("D:/Code/vehicel_plate/tong/yologru_hyperlpr_tong.txt","r",encoding='utf-8-sig')
out2 = open("D:/Code/vehicel_plate/tong/hyperlpr_yologru_tong.txt","r",encoding='utf-8-sig')

#out = open("D:/Code/vehicel_plate/error_yolo_gru.txt","a",encoding='utf-8')
lines = out1.readlines()
lines2 = out2.readlines()
tong1 = []
tong2 = []

for line in lines:
    
    li  = line.strip().split(',')
    filename1 = li[0]
    plate1 = li[1]
    label1 = filename1+','+plate1
    tong1.append(filename1)
print(len(tong1))

for line2 in lines2:
    li2  = line2.strip().split(',')
    filename2 = li2[0]
    plate2 = li2[1]
    label2 = filename2+','+plate2
    tong2.append(filename2)
#求交集的两种方式        
retA = [i for i in tong1 if i in tong2]      
print(retA)


