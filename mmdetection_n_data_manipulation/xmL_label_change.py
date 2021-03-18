import os
import re
import cv2
srcdir=r'D:\Infomize\AI\Annotations\For_training\13-Nov\table_entity_23_nov\data_24_nov\VOCdevkit\VOC2007\Annotations'
# desdir=r'D:\Infomize\AI\Annotations\table\Combined_data_Oct_table_v4\VOCdevkit\VOC2007\JPEGImages'
	
for xml_file in os.listdir(srcdir):
	with open(os.path.join(srcdir,xml_file),'r') as f:
			content= f.read()
	print(xml_file)
	# img = cv2.imread(os.path.join(desdir,os.path.splitext(xml_file)[0]+'.jpg'))
	# label1='table'
	# label2='header'
	# label3='footer'
	# label4='total'
	label5='Currency'
	label6='HeaderRemarks1'
	# content= content.replace('<name>Table_header</name>','<name>{}</name>'.format(label2))
	# content= content.replace('<name>Table</name>','<name>{}</name>'.format(label1))
	# content= content.replace('<name>hedaer</name>','<name>{}</name>'.format(label2))
	# content= content.replace('<name>Table_Footer</name>','<name>{}</name>'.format(label3))
	# content= content.replace('<name>Total_Value</name>','<name>{}</name>'.format(label4))
	# content= content.replace('<name>currency</name>','<name>{}</name>'.format(label5))
	# content= content.replace('<name>HeaderRemarks 1</name>','<name>{}</name>'.format(label6))
	content= content.replace('<depth>3</depth>','<depth>1</depth>')	



	with open(os.path.join(srcdir,xml_file),'w') as f:
		f.write(content)
	# break	
