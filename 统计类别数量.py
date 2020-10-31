# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:40:42 2019

@author: Administrator
"""
import os

def main():
    f = open('tongji_files.txt', 'w')
    path = 'G:/my_data/vel_train2'

#将文件名输出到txt文件
    for _, _, files in os.walk(path):
        for n in files:
            line = n+'\n'
            #f.write(line)

#统计文件夹内子文件夹及其文件的个数
    _, dirs, _ = next(os.walk(path))
    print('%s 中有 %d 个文件夹' % ('books', len(dirs)))
    for i in range(len(dirs)):
        dir_path = path + '/' + dirs[i]
        _, _, files = next(os.walk(dir_path))
        print('%s 中有 %d 个文件' % (dirs[i],len(files)))
        f.write('%s,%d\n' %(dirs[i],len(files)))

if __name__ == '__main__':
    main()
