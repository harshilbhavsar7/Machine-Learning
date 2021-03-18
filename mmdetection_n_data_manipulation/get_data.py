import os
srcdir=r'C:\Users\Dell\Downloads\data'
import shutil 
import xml.etree.ElementTree as ET
import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def get_data(img,configuration):
	data = pytesseract.image_to_data(img,config = configuration)
	data = data.split('\n')[1:]
	all_data = dict()
	for element in data:
		element = element.split('\t')
		#print(len(element[-1]))
		if element[-1] != '' or element[-1] == ' ':
			
			all_data[int(element[6]),int(element[7]),int(element[6])+int(element[8]),int(element[7])+int(element[9])] = element[-1]
	return all_data


all_data=dict()
headers=[]
count=0
for xml_file in os.listdir(srcdir):
	try:
		if xml_file.endswith('.xml'):

			image = os.path.join(srcdir,os.path.splitext(xml_file)[0]+'.jpg')
			img = cv2.imread(image)
			print(xml_file)
			count+=1
			print(count)
			tree = ET.parse(os.path.join(srcdir,xml_file))
			root = tree.getroot()
			for member in root.findall("object"):
				#classes_names.append(member[0].text)
				class_name = member[0].text
				if class_name !='table': 	
					x1 = int(member[4][0].text)
					y1 = int(member[4][1].text)
					x2 = int(member[4][2].text)
					y2 = int(member[4][3].text)
					configuration = ("-l eng --oem 1 --psm 11")
					cropped_img = img[y1:y2,x1:x2]
					data = get_data(cropped_img,configuration)
					for element in data.values():
						all_data[element] = class_name
			print('success')
					
	except Exception as e:
		print('Failed')
		print('Exception is ',e)


import pandas as pd
data = pd.DataFrame(list(zip(all_data.keys(),all_data.values())),columns=['token','class'])
data.to_csv('token_data.csv',index=False)
