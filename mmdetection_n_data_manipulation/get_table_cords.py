import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
tables=[]

for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\For_training\13-Nov\table_entity_23_nov\data_24_nov\VOCdevkit\VOC2007\Annotations" + "/*.xml"):
	print(xml_file)
	tree = ET.parse(xml_file)
	# print(tree)
	root = tree.getroot()
	for member in root.findall("object"):
		# print("in for")
		name=member.find("name").text
		# print(name)
		if name=="table":
			# print("table found")
			bnd_box = member.find("bndbox")
			bbox=[int(float(bnd_box.find("xmin").text)),int(float(bnd_box.find("ymin").text)),int(float(bnd_box.find("xmax").text)),int(float(bnd_box.find("ymax").text))]
			# print(bbox)
			tables.append(bbox)
			
print(len(tables))
print(tables[0][0])