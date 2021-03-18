import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


classes_names = []
xml_list = []
 
for xml_file in glob.glob(r"D:\Infomize\AI\Annotations\table\test_dhruv\Annotations" + "/*.xml"):
	print(xml_file)
	tree = ET.parse(xml_file)
	root = tree.getroot()
	for member in root.findall("object"):
		if(member[0].text=='header' or member[0].text=='total'):
			jpgsrc=r"D:\Infomize\AI\Annotations\table\test_dhruv\JPEGImages"
			xmlsrc=r"D:\Infomize\AI\Annotations\table\test_dhruv\Annotations"
			try:
				os.remove(os.path.join(jpgsrc,os.path.splitext(xml_file)[0]+'.jpg'))
			except:
				print("Jpeg of :"+xml_file+"is not found")
			try:
				os.remove(os.path.join(xmlsrc,xml_file))
			except:
				print("xml_not found: ",xml_file)
		# classes_names.append(member[0].text)
# classes_names = list(set(classes_names))
# classes_names.sort()
# print("Class length", len(classes_names))
# print(classes_names)