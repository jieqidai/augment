# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:56:38 2019

@author: A
"""
import sys
import importlib
importlib.reload(sys)

import csv
from xml.etree.ElementTree import iterparse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class XML_CSV():
    def read_csv_to_xml(self,csv_file,xmlfile):
        #逐行读取CSV文件的内容，将内容写进以internalid为键，name，sumary，steps，expectresult为值得字典
        csv_file = file(csv_file,'rb')
        reader = csv.reader(csv_file)  
        case_dic = {}  
        for line in reader:  
            if reader.line_num == 1:  
                continue  
            if line[0] == "testcase":
                name = str(line[1])
                internalid = str(line[4])
                summary = line[6]
                steps = line[7]
                expectedresults = line[8]
                case_dic[internalid] = (name,summary,steps,expectedresults)
        csv_file.close()
        print(case_dic)
        #用ElementTree方法打开xml文件，逐行解析XML文件，发现case为tag的行，就将name，sumary，steps，expectresult，这几项用字典的值替换。
        tree = ET.ElementTree()
        tree.parse(xmlfile)
        root = tree.getroot()
        root_suite_name = root.attrib['name']
         
        for node in tree.iter():
            if node.tag == "testsuite":
                print(node.attrib['name'])
                sub_suite_name = node.attrib['name']
                if sub_suite_name == root_suite_name:
                    sub_suite_name = ""
                for child in node:
                    if child.tag == "node_order":
                        #print child.text
                        pass
                    if child.tag == "details":
                        pass
            if node.tag == "testcase":
                new_internalid = node.attrib['internalid']
                #将根目录和子目录的名字都写进了case名字中。如果不需要可以用下面那行注释掉的替换这一行
                node.attrib['name'] = root_suite_name+'_'+sub_suite_name+'_'+case_dic[new_internalid][0]
                #node.attrib['name'] = case_dic[new_internalid][0]
                print(node.attrib['name'])
                #解析tag为testcase的节点的子节点，并修改节点的值
                for child in node:
                    if child.tag == "node_order":
                        pass
                    if child.tag == "externalid":
                        pass
                    if child.tag == "summary":
                        child.text = case_dic[new_internalid][1]
                        child.text = str(child.text.replace('\n',"<p>"))
                    if child.tag == "steps":
                        child.text = str(case_dic[new_internalid][2])
                        child.text = str(child.text.replace('\n',"<p>"))
                    if child.tag == "expectedresults":
                        child.text = case_dic[new_internalid][3]
                        child.text = str(child.text.replace('\n',"<p>"))
        #将修改后的ElementTree对象写入xml文件中。
        tree.write(xmlfile,encoding='utf8')   

if __name__ == "__main__":
    test = XML_CSV()
    #test.read_xml_to_csv('testsuites2.csv','testsuites.xml')
    test.read_csv_to_xml('testsuites2.csv','testsuites.xml')
 