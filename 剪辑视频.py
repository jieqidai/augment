# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:20:11 2020

@author: Administrator
"""

from moviepy.editor import*
# 剪辑50-60秒的音乐 00:00:50 - 00:00:60
video =CompositeVideoClip([VideoFileClip("D:/BaiduNetdiskDownload/算法锤练视频（公开）/1200w场景A常态视频/03000001006000000.mp4").subclip(0,60)])
# 写入剪辑完成的音乐
video.write_videofile("03000001006000000-0-60.mp4")