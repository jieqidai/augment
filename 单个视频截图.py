# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:44:29 2020

@author: Administrator
"""

import cv2
c = 1
path = '05-61-400-500-stop.mp4'
savepath = 'E:/AI_shipinjietu/'
vc = cv2.VideoCapture('E:/AI算法比赛/第一套算法事件视频/05-61-400-500-stop.mp4') #读入视频文件
if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
else:
    rval = False

timeF = 50  #视频帧计数间隔频率

while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        #name = path.split('/')[-1]
        print(c)
        #print(path[:-4])
        cv2.imwrite(savepath + path[:-4] + '_' + str(c) + '.jpg',frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()