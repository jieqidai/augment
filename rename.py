# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:08:51 2019

@author: A
"""

import os
import time
def changeImgName(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        filePath = os.path.split(path)           #分割出目录与文件
        fileMsg = os.path.splitext(filePath[1]) #分割出文件与文件扩展名
        fileExt = fileMsg[1]                     #取出后缀名(列表切片操作)
        fileName = fileMsg[0]                       #取出文件名
        imgExtList = ['bmp','jpeg','gif','png','jpg'] #常见文件名
        if fileExt.strip('.') in imgExtList:
            #os.rename(path, filePath[0]+os.sep+fileName.replace("京", "dk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("沪", "dj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("津", "dh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("渝", "dn")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("冀", "qk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("晋", "qj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("蒙", "qh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("辽", "qn")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("吉", "ek")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("黑", "ej")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("苏", "eh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("浙", "en")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("皖", "rk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("闽", "rj")+fileExt) #重命名
            #os.rename(path, filePath[0]+os.sep+fileName.replace("赣", "rh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("鲁", "rn")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("豫", "wk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("鄂", "wj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("湘", "wh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("粤", "wn")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("桂", "ak")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("琼", "aj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("川", "ah")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("贵", "an")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("云", "sk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("藏", "sj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("陕", "sh")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("甘", "sn")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("青", "fk")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("宁", "fj")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("新", "fh")+fileExt)
            
            #os.rename(path, filePath[0]+os.sep+fileName.replace("港", "a")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("学", "b")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("警", "d")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("澳", "e")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("挂", "f")+fileExt)
            #os.rename(path, filePath[0]+os.sep+fileName.replace("领", "g")+fileExt)
            os.rename(path, filePath[0]+os.sep+fileName.replace("test", "")+fileExt)
            i += 1
    elif os.path.isdir(path):#递归处理
        for x in os.listdir(path):
            changeImgName(os.path.join(path, x)) #os.path.join()路径处理

time.clock()
i = 0
changeImgName('D:/Code/vehicel_plate/FakeLPR/train/datasets/test')
print('程序运行耗时:%0.2f'%(time.clock()))
print('总共处理了 %s 张图片'%(i))