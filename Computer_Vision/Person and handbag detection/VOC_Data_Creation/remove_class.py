import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
 
for xml_file in glob.glob(r"D:\Harshil\My_work\ML\Projects\P_H_Object_detection\VOC\annot_data" + "/*.xml"):
	# print(xml_file)
	tree = ET.parse(xml_file)
	root = tree.getroot()
	keep_class=['person','handbag']
	
	for member in root.findall("object"):
		# classes_names.append(member[0].text)
		try:
			if member[0].text not in keep_class:
				print(member[0].text)
				root.remove(member)
			else:
				member[4][0].text=str(int(float(member[4][0].text)))
				member[4][1].text=str(int(float(member[4][1].text)))
				member[4][2].text=str(int(float(member[4][2].text)))
				member[4][3].text=str(int(float(member[4][3].text)))
		except:
			print(xml_file,member)
	tree.write(xml_file)