import os
srcdir=r'D:\Infomize\AI\Annotations\30-Oct-2020\table\useless\21_tnh_data\VOCdevkit\VOC2007\Annotations'
import xml.etree.ElementTree as ET
for xml_file in os.listdir(srcdir):
	# print(xml_file)
	tree = ET.parse(os.path.join(srcdir,xml_file))
	classes_names=[]	
	root = tree.getroot()
	
	for member in root.findall("object"):
		classes_names.append(member[0].text)
	if classes_names==[]:
		try:
			os.remove(os.path.join(srcdir,xml_file))
			os.remove(os.path.join('JPEGImages',os.path.splitext(xml_file)[0]+'.jpg'))
			print(xml_file+'is removed')		
		except Exception as e:
			print('In '+xml_file+' an exception occured : ')
			# os.remove(os.path.join('JPEGImages',os.path.splitext(xml_file)[0]+'.jpg'))


