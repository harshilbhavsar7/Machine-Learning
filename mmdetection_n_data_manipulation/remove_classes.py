# import os
# import re
# import cv2
# srcdir=r'D:\Infomize\AI\Annotations\30-Oct-2020\table\useful\test'
# # desdir=r'D:\Infomize\AI\Annotations\table\Combined_data_Oct_table_v4\VOCdevkit\VOC2007\JPEGImages'
	
# for xml_file in os.listdir(srcdir):
# 	with open(os.path.join(srcdir,xml_file),'r') as f:
# 			content= f.read()
# 	print(xml_file)
# 	# img = cv2.imread(os.path.join(desdir,os.path.splitext(xml_file)[0]+'.jpg'))
# 	# width = img.shape[1]
# 	# height = img.shape[0]
	
# 	# content= content.replace('<width>2000</width>','<width>{}</width>'.format(width))
# 	# content= content.replace('<height>2000</height>','<height>{}</height>'.format(height))
# 		with open(os.path.join(srcdir,xml_file),'w') as f:
# 			f.write(content)
# 	# break	
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
 
for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\30-Oct-2020\table\useful\table_new_structure" + "/*.xml"):
	print(xml_file)
	tree = ET.parse(xml_file)
	root = tree.getroot()
	delete_classes=['total','header','footer']
	for member in root.findall("object"):
		# classes_names.append(member[0].text)
		if(member[0].text=='total' or member[0].text=='header' or member[0].text=='footer' or member[0].text=='hedaer'):
			root.remove(member)
	tree.write(xml_file)
# classes_names = list(set(classes_names))
# classes_names.sort()
# print("Class length", len(classes_names))
# print(classes_names)