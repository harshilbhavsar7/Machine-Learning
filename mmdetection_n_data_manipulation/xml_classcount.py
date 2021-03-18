import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
count=0


for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\entities\test2\Annotations" + "/*.xml"):
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    tmp=[]
    for member in root.findall("object"):
        # classes_names.append(member[0].text)
        tmp.append(member[0].text)
    # print(tmp)
    if 'cell' not in tmp:
        print(xml_file,'is deleted')
        os.remove(xml_file)
        count=count+1
print(count,'files removed')
# classes_names = list(set(classes_names))
# classes_names.sort()
# print("Class length", len(classes_names))
# print(classes_names)