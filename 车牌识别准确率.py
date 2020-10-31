# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:05:58 2019

@author: A
"""
f1 = open("D:/Code/Vehicle-Car-detection-and-multilabel-classification-master/PyTorch-YOLOv3/plate_label.txt","r",encoding='utf-8-sig')
f2 = open("D:/Code/chinese_ocr-master/plate_result2.txt","r",encoding='utf-8-sig')

#out = open("D:/Code/vehicel_plate/error_yolo_gru.txt","a",encoding='utf-8')
lines = f1.readlines()
lines2 = f2.readlines()
i = 0
j =0

tong = []
bu = []
#out = open("D:/Code/vehicel_plate/tong/hyperlpr_gru_yolo_tong.txt","w",encoding='utf-8')
for line in lines:
    
    li  = line.strip().split(',')
    filename1 = li[0]
    plate1 = li[1]
    label1 = filename1+','+plate1

    for line2 in lines2:
        li2  = line2.strip().split(',')
        filename2 = li2[0]
        plate2 = li2[1]
        label2 = filename2+','+plate2
        
        
        #if filename1 ==filename2:
            #pla1 = plate1
            #pla2 = plate2
            
        if label1 == label2:
            tong.append(label1)
            #out.writelines(label1+'\n')
            #print(len(tong))
            j+=1
        #if filename1 == filename2 and plate1!=plate2 :
           # bu.append(filename2+','+plate2)
           # print(filename2,plate2)
    i+=1
#out.close()
#print(error)
#for k in range(0,len(tong)):    
#    out.writelines(tong[k]+'\n')
#out.close()    
print(i,j)
acc = j/i*100
print('acc: %f%%' % acc)
            
