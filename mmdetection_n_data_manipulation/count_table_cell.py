import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
fi_count=0
fi_name=[]
 
for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\entities\test2\Annotations" + "/*.xml"):
    # print(xml_file)
    tb_count=0
    de_count=0
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall("object"):
        # classes_names.append(member[0].text)
        class_name=member[0].text
        if(class_name=='table'):
            tb_count=tb_count+1
        if(class_name=='description'):
            de_count=de_count+1
    if tb_count>de_count and de_count!=0:
        fi_name.append(xml_file)
        fi_count=fi_count+1
print(fi_name)
print(fi_count)
# print(count,'files removed')
# classes_names = list(set(classes_names))
# classes_names.sort()
# print("Class length", len(classes_names))
# print(classes_names)