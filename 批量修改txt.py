# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:06:09 2019

@author: A
"""
          
import os

 
fileDir = "val_cocoperson2/"
fileList = os.listdir(fileDir)

pers = 0
car = 0
bus =0
truck=0 
for fileObj in fileList:

    name = fileObj
    if name.endswith(".txt"):
        #print(name)
        
        f = open(os.path.join(fileDir,name), 'r')
        lines = f.readlines() #整行读取
        f.close()
        #newfile=open('val_cocoperson2/%s'%(name),'w')
        #if not os.path.exists(newfile):
        #    os.makedirs(newfile)

        for line in lines:
            rs = line.rstrip('\n') #去除原来每行后面的换行符，但有可能是\r或\r\n
            rs = rs.split(' ')

            #if rs[0]=='0':                
            #    pers+=1
            #elif rs[0]=='1':                
             #   car +=1
            #elif rs[0]=='2':                
            #    bus+=1
            #elif rs[0]=='3':                
            #    truck+=1
                
#print(pers,car,bus,truck)
 
 
           
            #print(rs[0])
            #newfile.write("%s %s %s %s %s\n"%('0',rs[1],rs[2],rs[3],rs[4]))
            if rs[0] !='0':  
                print(fileObj)
                with open('error.txt', 'w') as f:
                    f.write(fileObj)
                #newname=('0'+' '+rs[1]+' '+rs[2]+' '+rs[3]+' '+rs[4])
                #newfile.write("%s %s %s %s %s\n"%(rs[0] ,rs[1],rs[2],rs[3],rs[4]))
            #elif rs[0]=='1':                
                #newname=('1'+' '+rs[1]+' '+rs[2]+' '+rs[3]+' '+rs[4])
            #    newfile.write("%s %s %s %s %s\n"%('0',rs[1],rs[2],rs[3],rs[4]))
            #elif rs[0]=='2':                
            #    continue
            #elif rs[0]=='3':                
            #    #newname=('2'+' '+rs[1]+' '+rs[2]+' '+rs[3]+' '+rs[4])
            #    newfile.write("%s %s %s %s %s\n"%('2',rs[1],rs[2],rs[3],rs[4]))
            #elif rs[0]=='4':                
                #newname=('4'+' '+rs[1]+' '+rs[2]+' '+rs[3]+' '+rs[4])
             #   newfile.write("%s %s %s %s %s\n"%('3',rs[1],rs[2],rs[3],rs[4]))
            #else:
            #    newname=rs.replace(rs,'5'+' '+rs[1]+' '+rs[2]+' '+rs[3]+' '+rs[4]+'\n')
            
            #newfile.write(newname+'\n')
        #newfile.close()

 