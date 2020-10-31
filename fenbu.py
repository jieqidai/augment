# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:25:35 2020

@author: Administrator
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Titanic数据集
titanic = pd.read_csv('car.csv')
# 检查年龄是否有缺失any(titanic.Age.isnull())
# 不妨删除含有缺失年龄的观察
titanic = titanic[titanic['area']<=1000]
#titanic.dropna(subset=['area'], inplace=True)
df = titanic.reindex(titanic['area'].abs().sort_values(ascending=True).index)
df = df[df['area']>=100]

length = len(df)
print(length)
for i in range(0,length):
    
    if i/len(df) == 0.3:
        print(df['area'])
    if i/len(df) == 0.4:
        print(df['area'])
    if i/len(df) == 0.5:
        print(df['area'])
    if i/len(df) == 0.6:
        print(df['area'])

# 设置图形的显示风格
plt.style.use('ggplot')
plt.xlim(0, 1000)
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率

plt.hist(titanic.area, # 绘图数据
        bins = np.arange(0,1000,5),#bins = np.arange(titanic.area.min(),titanic.area.max(),10), # 指定直方图的组距
        density = True, # 设置为频率直方图
        color = 'steelblue', # 指定填充色
        edgecolor = 'k') # 指定直方图的边界色

# 设置坐标轴标签和标题
plt.title('car面积大小直方图')
plt.xlabel('面积大小')
plt.ylabel('频率')

# 生成正态曲线的数据
#x1 = np.linspace(titanic.area.min(), titanic.area.max(), 1000)
x1 = np.linspace(0, 1000, 10)
normal = norm.pdf(x1, titanic.area.mean(), titanic.area.std())
# 绘制正态分布曲线
line1, = plt.plot(x1,normal,'r-', linewidth = 2) 

# 生成核密度曲线的数据
kde = mlab.GaussianKDE(titanic.area)
x2 = np.linspace(0, 1000, 10)
# 绘制
line2, = plt.plot(x2,kde(x2),'g-', linewidth = 2)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')

# 显示图例
plt.legend([line1, line2],['正态分布曲线','核密度曲线'],loc='best')
plt.savefig('car.jpg',dpi = 300)
# 显示图形
plt.show()