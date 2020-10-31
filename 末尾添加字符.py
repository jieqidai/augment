# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:36:01 2019

@author: A
"""

From_file=open('H:/数据集/打逃数据/jietu/京珠北卡口2016年数据1/京珠北卡口2016年数据1分析结果_plate/images10_plate_total.txt',encoding='utf-8')
f=open('H:/数据集/打逃数据/jietu/京珠北卡口2016年数据1/京珠北卡口2016年数据1分析结果_plate/images10_8位车牌2.txt','a',encoding = 'utf-8')
count=0
huancun=[]
for each_line in From_file:
    #print(type(each_line))  each_line 是字符类型
    
    plate = each_line.split(',')
    if plate[-1]==u'绿\n' or len(plate[-2])>7:
        f.writelines(each_line)

f.close()
From_file.close()
print('文件中总共有：%d行'%count)
