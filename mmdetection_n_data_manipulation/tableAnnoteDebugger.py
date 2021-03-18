import csv
import xml.etree.ElementTree as ET
import os
from os import listdir
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--source", '-s', type=str, help="Provide the input path of the source directory")
args = parser.parse_args()

input_dir = args.source
# print('input_dir:', input_dir)

main_dir = os.path.join(input_dir,'Main')
img_dir = os.path.join(input_dir,'JPEGImages')
xml_dir = os.path.join(input_dir,'Annotations')


def plotDeugger(child, img_path, tag):
	temp_img = cv2.imread(img_path)
	for child in root:
			if child.tag == 'object':
				if child.find('name').text == tag:
					xmin, ymin, xmax, ymax = getCoords(child)
					# print(str(xmin) +", "+ str(ymin) +", "+	 str(xmax) +", "+ str(ymax))
					cv2.rectangle(temp_img, (xmin, ymin), (xmax, ymax), color=(255, 0, 0), thickness=5)
					cv2.putText(temp_img, tag, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1.75, (0, 0, 255), 3)
	cv2.imshow(os.path.basename(img_path), cv2.resize(temp_img, (700, 900)))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def rectArea(coords):
	(xmin, ymin, xmax, ymax) = coords
	area = (xmax-xmin)*(ymax-ymin)
	return area

def getCoords(child):
	# for child in root:
	# 		if child.tag == 'object':
	# 			if child.find('name').text == tag:
	xmin = int(child.find('bndbox/xmin').text)
	ymin = int(child.find('bndbox/ymin').text)
	xmax = int(child.find('bndbox/xmax').text)
	ymax = int(child.find('bndbox/ymax').text)
	return xmin, ymin, xmax, ymax





improper_data = []
incomplete_data = []
null_data = []
taglist = []

max_table_size = 0
max_cell_size = 0
max_description_size = 0

'''1. read txt file in the Main folder.
	This is to check if the file and folder structuring has been done properly.
'''
for file in listdir(main_dir):
	print('\nScanning ', file)
	txt_file = open(os.path.join(main_dir,file), 'r')
	Lines = txt_file.readlines()

	# file = os.path.splitext(file)[0]
	new_file_content = ""
	for line in Lines:
		table_size = 0
		cell_size = 0
		description_size = 0

		img_path = os.path.join(img_dir,line.strip()+'.jpg')
		xml_path = os.path.join(xml_dir,line.strip()+'.xml')

		# print('img_path:', os.path.basename(img_path))
		# print('xml_path:', os.path.basename(xml_path))

		'''2. Check if the respective files exist of not.'''
		if not os.path.exists(img_path):
			print('Image doesnot exists: ', img_path)
			improper_data.append(img_path)
		if not os.path.exists(xml_path):
			print('XML doesnot exists: ', xml_path)
			improper_data.append(xml_path)

		tree = ET.parse(xml_path)
		root = tree.getroot()

		# print('filename:', tree.find('filename').text)
		# print('path:', os.path.basename(tree.find('path').text))

		'''3. verify the image name is same as in XML path and image tag.'''
		if tree.find('filename').text != os.path.basename(tree.find('path').text):
			print(os.path.basename(img_path), ' doesnot match')
		elif os.path.basename(tree.find('path').text) != os.path.basename(img_path):
			print(os.path.basename(img_path), ' doesnot match')

		'''4. Check objects in xml file. Print how many Object tags exists in XML and their values.
		If no object count detected, the file is carring 'null' data.
		'''
		obj_count = 0
		# print(tree.find('object/name').text)
		for child in root:
			if child.tag == 'object':
				# print(child.find('name').text)
				obj_count += 1
			# print(child.tag, child.attrib)
		if obj_count == 0:
			null_data.append([os.path.splitext(file)[0], os.path.basename(xml_path), 'no object found!'])
		# else:
		# 	print(obj_count, 'objects found.')
		# print([elem.tag for elem in root.iter()])

		table_list = []
		cell_list = []
		description_list = []

		'''5. Check all the object names in the dataset. 
		If more number of labels are found than what is expected, that means, wrong labeling had been done.
		'''
		for child in root:
			if child.tag == 'object':
				if len(taglist)==0 or child.find('name').text not in taglist:
					taglist.append(child.find('name').text)

				# for child in root:
				# 	if child.tag == 'object':
				if child.find('name').text == 'table':
					# print(child.find('name').text)
					table_size += 1
					table_list.append(getCoords(child))
				if child.find('name').text == 'cell':
					# print(child.find('name').text)
					cell_size += 1
					cell_list.append(getCoords(child))
				if child.find('name').text == 'description':
					# print(child.find('name').text)
					description_size += 1
					description_list.append(getCoords(child))

		'''9. Check and verify Height and Width of the input image.'''
		temp_img = cv2.imread(img_path)
		if tree.find('size/width').text != str(temp_img.shape[1]) or tree.find('size/height').text != str(temp_img.shape[0]):
			print('H&W error in ', line)


		'''6. Get maximum number of labels in every data.
		If number of predefined labes exceeds its limits, then there could be bug in the dataset.
		'''
		if table_size > max_table_size:
			max_table_size = table_size
		if cell_size > max_table_size:
			max_cell_size = cell_size
		if description_size > max_table_size:
			max_description_size = description_size

		# '''Temporary debug module'''
		# if max_table_size>5:
		# 	print('>>>>>>', line)
		# 	exit()

		'''7.1. If there is no table, its a buggy data. Because there has to be one table in every data file.'''
		# if table_size == 0:
		# 	incomplete_data.append([os.path.splitext(file)[0], os.path.basename(xml_path), 'table not found in xml'])
			# inc_img = cv2.imread(img_path)
			# cv2.imwrite('D:/Tarun_workspace/table_data/13k_table_data/VOCdevkit/VOC2007/temp_annote/'+os.path.basename(img_path), inc_img)
			# print('table not found for ', os.path.basename(img_path))
		'''7.2. If there is no cell, its a buggy data. Because there has to be minimum one cell in every data file.'''
		# if cell_size == 0:
		# 	incomplete_data.append([os.path.splitext(file)[0], os.path.basename(xml_path), 'cell not found in xml'])
			# print('cell not found for ', img_path)

		'''7.3. Check improper table data.
			-> 1) Mostly there is only one table in a xml file.
			-> 2) Check for more than one table. It can be a case of wrong labeling.
		'''
		if cell_size>1 and table_size==0:
			incomplete_data.append([os.path.splitext(file)[0], os.path.basename(xml_path), 'cell is there but not table'])
		if table_size > 1 or improper_data==0:
			improper_data.append([os.path.splitext(file)[0], os.path.basename(xml_path), 'table_size:'+str(table_size)])
			# plotDeugger(child, img_path, 'table')
			# print('\nVerify image: ', os.path.basename(img_path))
			# print('table_size', table_size)
			# temp_img = cv2.imread(img_path)
			# cv2.imshow('Verify image: ', cv2.resize(temp_img, (700, 900)))
			# cv2.waitKey(1000)


		table_size = 0
		cell_size = 0
		description_size = 0

		'''8. Compare cell and description area with table area. 
		If the former is smaller than the priors, there's a bug in the data.
		'''
		if len(table_list)>1:
			# excluding identified files
			continue
		for table in table_list:
			table_area = rectArea(table)
			for cell in cell_list:
				cell_area = rectArea(cell)
				if cell_area > table_area:
					temp_img = cv2.imread(img_path)
					xmin, ymin, xmax, ymax = cell
					cv2.rectangle(temp_img, (xmin, ymin), (xmax, ymax), color=(0, 0, 255), thickness=5)
					cv2.putText(temp_img, 'cell', (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1.75, (0, 0, 255), 3)
					cv2.imshow(os.path.basename(img_path), cv2.resize(temp_img, (700, 900)))
					cv2.waitKey(0)
					cv2.destroyAllWindows()
			for des in description_list:
				des_area = rectArea(cell)
				if des_area > table_area:
					temp_img = cv2.imread(img_path)
					xmin, ymin, xmax, ymax = des
					cv2.rectangle(temp_img, (xmin, ymin), (xmax, ymax), color=(0, 0, 255), thickness=5)
					cv2.putText(temp_img, 'description', (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1.75, (0, 0, 255), 3)
					cv2.imshow(os.path.basename(img_path), cv2.resize(temp_img, (700, 900)))
					cv2.waitKey(0)
					cv2.destroyAllWindows()


print('\ntags:', taglist)
print('\nmax no. of table:', max_table_size)
print('max no. of cell:', max_cell_size)
print('max no. of description:', max_description_size)
# print(improper_data, end=' ')
if len(incomplete_data)>0 or len(improper_data)>0 or len(null_data)>0:
	print("\n!!!Caution: Improper data!!!\n")
	print(incomplete_data)
	print(len(incomplete_data))
else:
	print('\nNo issue found!!! You are clear to use this data.')
# for data in incomplete_data: print(data)
# print()
for data in improper_data: 
	print(data)
for data in null_data: 
	print(data)