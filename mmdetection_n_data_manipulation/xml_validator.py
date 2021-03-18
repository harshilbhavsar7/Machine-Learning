import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
 
for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\For_training\13-Nov\table_entity_23_nov\data_24_nov\VOCdevkit\VOC2007\Annotations" + "/*.xml"):
	print(xml_file)
	tree = ET.parse(xml_file)
	root = tree.getroot()
	for member in root.findall("object"):
		classes_names.append(member[0].text)
classes_names = list(set(classes_names))
classes_names.sort()
print("Class length", len(classes_names))
print(classes_names)