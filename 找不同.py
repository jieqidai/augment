# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:47:40 2019

@author: A
"""

f1 = open("D:/Code/vehicel_plate/plate_hyperlpr_wan.txt","r",encoding='utf-8-sig')
f2 = open("D:/Code/vehicel_plate/plate_yolo_wan.txt","r",encoding='utf-8-sig')

#out = open("D:/Code/vehicel_plate/error_yolo_gru.txt","a",encoding='utf-8')
lines = f1.readlines()
lines2 = f2.readlines()
i = 0
j =0

tong1 = []
tong2 = []
out1 = open("D:/Code/vehicel_plate/tong/hyperlpr_hypergru_tong.txt","w",encoding='utf-8')
out2 = open("D:/Code/vehicel_plate/tong/hypergru_hyperlpr_tong.txt","w",encoding='utf-8')
for line in lines:
    
    li  = line.strip().split(',')
    filename1 = li[0]
    plate1 = li[1]
    label1 = filename1+','+plate1
    tong1.append(label1)


for line2 in lines2:
    li2  = line2.strip().split(',')
    filename2 = li2[0]
    plate2 = li2[1]
    label2 = filename2+','+plate2
    tong2.append(label2)
#求交集的两种方式        
retA = [i for i in tong1 if i in tong2]      
retB = list(set(tong1).intersection(set(tong2)))

print(len(retA))
#求并集
retC = list(set(tong1).union(set(tong2)))

#求差集，在B中但不在A中
retD = list(set(tong1).difference(set(tong2)))
retE = list(set(tong2).difference(set(tong1)))

retF = [i for i in retD if i in retE]
print(len(retD)) 
print(len(retE)) 
#for m in retD:
#    out1.writelines(m+'\n')
   
#out1.close()
#for n in retE:
#    out2.writelines(n+'\n')
#out2.close()


