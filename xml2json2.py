# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:55:57 2020

@author: Administrator
"""

#coding:utf-8
 
# pip install lxml
 
import os
import glob
import json
import shutil
import numpy as np
import xml.etree.ElementTree as ET
 
 
START_BOUNDING_BOX_ID = 1
 
 
def get(root, name):
    return root.findall(name)
 
 
def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.'%(name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.'%(name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars
 
 
def convert(xml_list, json_file):
    json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
    categories = pre_define_categories.copy()
    bnd_id = START_BOUNDING_BOX_ID
    all_categories = {}
    for index, line in enumerate(xml_list):
        # print("Processing %s"%(line))
        xml_f = line
        tree = ET.parse(xml_f)
        root = tree.getroot()
        
        filename = os.path.basename(xml_f)[:-4] + ".jpg"
        image_id = 20190000001 + index
        size = get_and_check(root, 'size', 1)
        width = int(get_and_check(size, 'width', 1).text)
        height = int(get_and_check(size, 'height', 1).text)
        image = {'file_name': filename, 'height': height, 'width': width, 'id':image_id}
        json_dict['images'].append(image)
        ## Cruuently we do not support segmentation
        #  segmented = get_and_check(root, 'segmented', 1).text
        #  assert segmented == '0'
        for obj in get(root, 'object'):
            #category = get_and_check(obj, 'name', 1).text
            category = 'vehicle'
            if category in all_categories:
                all_categories[category] += 1
            else:
                all_categories[category] = 1
            if category not in categories:
                if only_care_pre_define_categories:
                    continue
                new_id = len(categories) + 1
                print("[warning] category '{}' not in 'pre_define_categories'({}), create new id: {} automatically".format(category, pre_define_categories, new_id))
                categories[category] = new_id
            category_id = categories[category]
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(float(get_and_check(bndbox, 'xmin', 1).text))
            ymin = int(float(get_and_check(bndbox, 'ymin', 1).text))
            xmax = int(float(get_and_check(bndbox, 'xmax', 1).text))
            ymax = int(float(get_and_check(bndbox, 'ymax', 1).text))
            assert(xmax > xmin), "xmax <= xmin, {}".format(line)
            assert(ymax > ymin), "ymax <= ymin, {}".format(line)
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {'area': o_width*o_height, 'iscrowd': 0, 'image_id':
                   image_id, 'bbox':[xmin, ymin, o_width, o_height],
                   'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                   'segmentation': []}
            json_dict['annotations'].append(ann)
            bnd_id = bnd_id + 1
 
    for cate, cid in categories.items():
        cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat)
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()
    print("------------create {} done--------------".format(json_file))
    print("find {} categories: {} -->>> your pre_define_categories {}: {}".format(len(all_categories), all_categories.keys(), len(pre_define_categories), pre_define_categories.keys()))
    print("category: id --> {}".format(categories))
    print(categories.keys())
    print(categories.values())
 
 
if __name__ == '__main__':
    classes = ['vehicle']
    ''''person','other',
           'black_bus','black_car','black_truck','black_van','blue_bus','blue_car','blue_truck','blue_van','brown_bus','brown_car',
           'brown_truck','brown_van','green_bus','green_car','green_truck','green_van','grey_bus','grey_car','grey_truck','grey_van',
           'multi_bus','multi_car','orange_bus','orange_car','orange_truck','orange_van','pink_bus','pink_car','pink_truck','purple_bus',
           'purple_car','purple_truck','purple_van','red_bus','red_car','red_truck','red_van','silvery_bus','silvery_car','silvery_truck',
           'silvery_van','white_bus','white_car','white_truck','white_van','yellow_bus','yellow_car','yellow_truck','yellow_van']
           '''
    '''classes = ['person','other','multi_car_small','multi_bus_large',
               'black_bus_large','black_car_pickup','black_car_small','black_car_suv','black_lifter','black_police','black_truck_big','black_truck_bulk','black_truck_small','black_truck_tanker',
               'black_truck_trailer','black_van','blue_bus_large','blue_bus_medium','blue_car_pickup','blue_car_small','blue_car_suv','blue_truck_big','blue_truck_bulk','blue_truck_muck',
               'blue_truck_small','blue_truck_tanker','blue_truck_trailer','blue_van','brown_bus_large','brown_bus_medium','brown_car_pickup','brown_car_small','brown_car_suv','brown_truck_big',
               'brown_truck_bulk','brown_truck_small','brown_truck_tanker','brown_truck_trailer','brown_van','green_bus_large','green_car_pickup','green_car_small','green_car_suv','green_military',
               'green_truck_big','green_truck_bulk','green_truck_small','green_truck_tanker','green_truck_trailer','green_van','grey_bus_large','grey_bus_medium','grey_car_pickup','grey_car_small',
               'grey_car_suv','grey_truck_big','grey_truck_bulk','grey_truck_mixer','grey_truck_muck','grey_truck_small','grey_truck_tanker','grey_truck_trailer','grey_van','orange_bus_large',
               'orange_car_pickup','orange_car_small','orange_car_suv','orange_rescue','orange_truck_big','orange_truck_bulk','orange_truck_small','orange_truck_tanker','orange_truck_trailer','orange_van',
               'pink_bus_large','pink_car_small','pink_truck_big','purple_bus_large','purple_car_small','purple_car_suv','purple_truck_big','purple_truck_small','purple_truck_tanker','purple_truck_trailer',
               'purple_van','red_bus_large','red_car_pickup','red_car_small','red_car_suv','red_fire','red_lifter','red_truck_big','red_truck_bulk','red_truck_muck',
               'red_truck_small','red_truck_tanker','red_truck_trailer','red_van','silvery_bus_large','silvery_bus_medium','silvery_car_pickup','silvery_car_small','silvery_car_suv','silvery_escort ',
               'silvery_truck_big','silvery_truck_bulk','silvery_truck_small','silvery_truck_tanker','silvery_truck_trailer','silvery_van','white_ambulance','white_bus_large','white_bus_medium','white_car_pickup',
               'white_car_small','white_car_suv','white_lifter','white_police','white_rescue','white_truck_big','white_truck_bulk','white_truck_mixer','white_truck_muck','white_truck_small',
               'white_truck_tanker','white_truck_trailer','white_van','yellow_bus_large','yellow_bus_medium','yellow_car_pickup','yellow_car_small','yellow_car_suv','yellow_lifter','yellow_rescue',
               'yellow_truck_big','yellow_truck_bulk','yellow_truck_muck','yellow_truck_small','yellow_truck_tanker','yellow_truck_trailer','yellow_van','multi_truck_small','multi_truck_big']
    '''
    pre_define_categories = {}
    for i, cls in enumerate(classes):
        pre_define_categories[cls] = i + 1
    # pre_define_categories = {'a1': 1, 'a3': 2, 'a6': 3, 'a9': 4, "a10": 5}
    only_care_pre_define_categories = True
    # only_care_pre_define_categories = False
    

    save_json_train = 'instances_traindet.json'
    save_json_val = 'instances_valdet.json'
    #xml_dir = "./tmp_xml"
    
    xml_list_train = 'E:/data/DETRAC/detractrainxml'
    xml_list_val = 'E:/data/DETRAC/detracvalxml'
 
    xml_list_train = glob.glob(xml_list_train + "/*.xml")
    xml_list_val = glob.glob(xml_list_val + "/*.xml")
    #xml_list_train = np.sort(xml_list_train)
    #xml_list_val = np.sort(xml_list_val)
    
    print(len(xml_list_train))
    print(len(xml_list_val))
    
 
 
    train_num = int(len(xml_list_train))
    val_num = int(len(xml_list_val))
    xml_list_train = xml_list_train[0:]
    xml_list_val = xml_list_val[0:]
 
    convert(xml_list_train, save_json_train)
    convert(xml_list_val, save_json_val)
 
    print("-------------------------------")
    print("train number:", len(xml_list_train))
    print("val number:", len(xml_list_val))