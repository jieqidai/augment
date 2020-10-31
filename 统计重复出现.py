# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:28:37 2019

@author: A
"""
result= {}
with open("D:/Code/vehicel_plate/plate_yolo_gru_wan.txt","r",encoding='utf-8-sig') as fopen:
    fopen.seek(0,2)
    all = fopen.tell()
    fopen.seek(0,0)
    while fopen.tell() < all:
        lines = fopen.readline().strip().split(',')
        lines = lines[0]
        if lines in result:
            result[lines] += 1
        else:
            result[lines] = 1
aaa = sorted(result.items(),key=lambda k:k[1],reverse=True)
print(len(aaa))
f = open("D:/Code/vehicel_plate/plate_yolo_gru1.txt","w",encoding='utf-8')
for k in range(len(aaa)):
    
    if aaa[k][1]>1:
        f.writelines(aaa[k][0]+','+str(aaa[k][1])+'\n')
        #print(aaa[k][0])
f.close()

