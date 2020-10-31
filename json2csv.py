import json
import csv
import codecs
#import join
data_file = open('airplanes.csv', 'w', newline='')

jsonData = codecs.open('airplanes.json', 'r', 'utf-8')
# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
# csvfile = open(path+'.csv', 'wb') # python2下
csvfile = open('airplanes.csv', 'w', newline='') # python3下
writer = csv.writer(csvfile, delimiter=',')
flag = True
for line in jsonData:
    dic = json.loads(line[0:-1]) #json每行不能有多余的符号，如 ，、
    if flag:
    # 获取属性列表
        keys = list(dic.keys())
        print (keys)
        writer.writerow(keys) # 将属性列表写入csv中
        flag = False
    else:
        # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow(list(dic.values()))
jsonData.close()
csvfile.close()

