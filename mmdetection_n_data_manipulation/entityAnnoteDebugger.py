import csv
import xml.etree.ElementTree as ET
import os,shutil
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


def plotDeugger(root, img_path, tag):
	temp_img = cv2.imread(img_path)
	for child in root:
			if child.tag == 'object':
				xmin, ymin, xmax, ymax = getCoords(child)
				# print(str(xmin) +", "+ str(ymin) +", "+	 str(xmax) +", "+ str(ymax))
				cv2.rectangle(temp_img, (xmin, ymin), (xmax, ymax), color=(255, 0, 0), thickness=5)
				cv2.putText(temp_img, child.find('name').text, (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 1.75, (0, 0, 255), 3)
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


debugfiles = []
taglist = []
null_data = []
improper_data=[]
max_size_chart = {}

'''1. read txt file in the Main folder.
	This is to check if the file and folder structuring has been done properly.
'''
for file in listdir(main_dir):
	print('\nScanning ', file)
	txt_file = open(os.path.join(main_dir,file), 'r')
	print(file)
	Lines = txt_file.readlines()

	# file = os.path.splitext(file)[0]
	new_file_content = ""
	for line in Lines:
		size_chart = {}

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


		'''5. Check all the object names in the dataset. 
		If more number of labels are found than what is expected, that means, wrong labeling had been done.
		'''
		for child in root:
			if child.tag == 'object':
				'''Create TagList'''
				if len(taglist)==0 or child.find('name').text not in taglist:
					taglist.append(child.find('name').text)

				# for child in root:
				# 	if child.tag == 'object':
				if child.tag != 'table' and child.tag != 'cell' and child.tag != 'description':
					if child.find('name').text in size_chart:
						size_chart[child.find('name').text] += 1
					else:
						size_chart[child.find('name').text] = 1
		# plotDeugger(root, img_path,'label')

		# print(size_chart)
		for size in size_chart:
			# if size != 'cell' and size != 'description' and size!='Currency':
			if size !='Currency':
				if size_chart[size] > 1:
					debugfiles.append([size, size_chart[size], line])


		'''9. Check and verify Height and Width of the input image.'''
		temp_img = cv2.imread(img_path)
		if tree.find('size/width').text != str(temp_img.shape[1]) or tree.find('size/height').text != str(temp_img.shape[0]):
			print('H&W error in ', line)


		'''6. Get maximum number of labels in every data.
		If number of predefined labes exceeds its limits, then there could be bug in the dataset.
		'''
		# Check if dictonary is empty
		if not bool(max_size_chart):
			max_size_chart = size_chart
		else:
			for k, v in size_chart.items():
				if k not in max_size_chart:
					max_size_chart[k] = v
				elif v > max_size_chart[k]:
					# print(max_size_chart[k])
					max_size_chart[k] = v
				# else:
				# 	print('some error occured')

		size_chart = {}

# print('\ntags:')
# for tag in taglist: print("\t"+tag)

# print('\nmax no. of table:')
# for k, v in max_size_chart.items(): print("\t"+k+": ", v)

# print('\nDebug files:')
# for file in debugfiles: print("\b", file)

print('no. of files to change:', len(debugfiles))
print(debugfiles)
# defectivedes=r'D:\Infomize\AI\Annotations\For_training\17-Nov\data\VOCdevkit\VOC2007\def_des'
# try:
# 	# for i in range(len(debugfiles)):
# 	# 	# debugfiles[i][2].replace('\n','')
# 	# 	shutil.move(xml_dir+'/'+debugfiles[i][2].replace('\n','')+'.xml',defectivedes)
# 	# 	# print(xml_dir+'/'+debugfiles[i][2]+'.xml')
# 	for file in debugfiles:
# 		if os.path.exists(defectivedes+'/'+file[2].replace('\n','')+'.xml')==False:
# 			# print(xml_dir+'/'+file[2].replace('\n','')+'.xml')
# 			shutil.move(xml_dir+'/'+file[2].replace('\n','')+'.xml',defectivedes)
# except Exception as e:
# 	print(e)