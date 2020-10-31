# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:13:11 2019

@author: A
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:02:05 2017
@author: wq
"""
 
import pandas as pd
 
df1 = pd.read_csv(u'D:/data/plate.csv', encoding='utf-8')
 
 
df2 = pd.read_csv('D:/data/vehicle.csv', encoding='utf-8')
 
 
 
outfile = pd.merge(df1, df2, how='left', left_on=u'path',right_on='path')
 
outfile.to_csv('outfile.csv', index=False, encoding='gbk')