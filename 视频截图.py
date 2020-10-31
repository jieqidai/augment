# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:22:31 2019

@author: Administrator
"""
import os
import cv2

videoPath = "E:/AI算法比赛/第一套算法事件视频/"
savePath = "E:/AI算法比赛/shipinjietu/"
videolist = os.listdir(videoPath)

for video in videolist:
    c = 1
    videofile = videoPath + video
    vc = cv2.VideoCapture(videofile) #读入视频文件
    if vc.isOpened(): #判断是否正常打开
        rval , frame = vc.read()
    else:
        rval = False
        print("error")

    timeF = 50  #视频帧计数间隔频率

    while rval:   #循环读取视频帧
        rval, frame = vc.read()
        if(c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite(savePath + video[:-4] + '_' + str(c) + '.jpg',frame) #存储为图像
        c = c + 1
        cv2.waitKey(1)
    vc.release()