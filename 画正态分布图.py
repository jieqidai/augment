# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:53:25 2020

@author: Administrator
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#使用%matplotlib命令可以将matplotlib的图表直接嵌入到Notebook之中，或者使用指定的界面库显示图表，它有一个参数指定matplotlib图表的显示方式
#inline表示将图表嵌入到Notebook中。
#matplotlib inline

#为了使画出来的图支持 retina格式
#config InlineBackend.figure_format = 'retina'

data = pd.read_csv('bus.csv') #载入数据文件
data.head(5) #查看前5个头部数据

len(data) 

time = data["area"] #把数据集中的 time 定义为 time
mean = time.mean()
print(max(time))
#S.D.标准差，把数据集中的标准差 定义为 std
std = time.std()
print(std)

#正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

# x的范围为60-150，以1为单位,需x根据范围调试
x = np.arange(0, 60000,1)

# x数对应的概率密度
y = normfun(x, mean, std)

# 参数,颜色，线宽
plt.plot(x,y, color='g',linewidth = 3)

#数据，数组，颜色，颜色深浅，组宽，显示频率
plt.hist(time, bins =7, color = 'r',alpha=0.5,rwidth= 0.9)

plt.title('area distribution')
plt.xlabel('aera score')
plt.ylabel('Probability')
plt.show()