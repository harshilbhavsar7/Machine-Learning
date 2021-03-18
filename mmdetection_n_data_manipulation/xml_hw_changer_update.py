import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import cv2
import argparse

classes_names = []
xml_list = []
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', type=str, help='Source')
parser.add_argument('-d', '--des', type=str, help='Destination')

   

args = parser.parse_args()

# srcdir=r"D:\Infomize\AI\Annotations\table\Combined_new_table\JPEGImages"
# desdir=r"D:\Infomize\AI\Annotations\table\Combined_new_table\Main"
srcdir=args.src
desdir=args.des
 
for xml_file in glob.glob(srcdir + "/*.xml"):
	print(xml_file)
	tree = ET.parse(xml_file)
	root = tree.getroot()
	# print("test")
	# break
	for member in root.findall("size"):
			try:
				print('jpgsrc: ', desdir)
				# print('xml_file: ', os.path.basename(xml_file))
				path = os.path.join(desdir,os.path.splitext(os.path.basename(xml_file))[0])+'.jpg'
				# # print(">>>", path)
				im=cv2.imread(path)
				# cv2.imshow('test', im)
				# cv2.waitKey(0)
				# print(im.shape)
				member[1].text=str(im.shape[0])
				print(member[1])
				member[0].text=str(im.shape[1])
				print(member[2])
				# print("Succesfully changed size of :"+xml_file)
				# os.remove(os.path.join(jpgsrc,os.path.splitext(xml_file)[0]+'.jpg'))
			except Exception as e:
				print("error is "+str(e))
			# break
	print(xml_file)
	tree.write(xml_file)
	# break

			# try:
			# 	os.remove(os.path.join(xmlsrc,xml_file))
			# except:
			# 	# # print("xml_not found: ",xml_file)
		# classes_names.append(member[0].text)
# classes_names = list(set(classes_names))
# classes_names.sort()
# # # print("Class length", len(classes_names))
# # # print(classes_names)