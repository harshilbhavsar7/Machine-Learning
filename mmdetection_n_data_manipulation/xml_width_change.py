import os
import re
import cv2
srcdir=r'C:\Users\Dell\Downloads\test2\annotations'
desdir=r'C:\Users\Dell\Downloads\test2\images'
	
for xml_file in os.listdir(srcdir):
	with open(os.path.join(srcdir,xml_file),'r') as f:
			print('read')
			content= f.read()
	print(xml_file)
	img = cv2.imread(os.path.join(desdir,os.path.splitext(xml_file)[0]+'.jpg'))
	width = img.shape[1]
	height = img.shape[0]
	print(height,width)
	content= content.replace('<width>2000</width>','<width>{}</width>'.format(width))
	content= content.replace('<height>2000</height>','<height>{}</height>'.format(height))
	with open(os.path.join(srcdir,xml_file),'w') as f:
		f.write(content)
	# break	
