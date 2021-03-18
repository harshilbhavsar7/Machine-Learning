import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
from os import listdir
import argparse
import os
import cv2
import json
from shutil import copyfile		# copyfile(src, dst)

parser = argparse.ArgumentParser()
parser.add_argument("--source", '-s', type=str, help="Provide the path of annotation directory as source (which contains JSON files from SuperAnnote tool)")
parser.add_argument("--destination", '-d', type=str, help="Provide the path of destination file where output will be stored (This will contain all the JPEGImage and Annotation folder as VOC format)")

args = parser.parse_args()
source_dir = args.source
dest_dir = args.destination

def generateXML(img_name, data, tags):
	'''annotation'''
	root = ET.Element("annotation")
	'''filename'''
	fn = ET.Element("filename") 
	# fn.tail = "\n\t" 
	root.append(fn)
	fn.text = img_name

	'''path'''
	pth = ET.Element('path')
	root.append(pth)
	pth.text = os.path.join(image_dir, img_name)

	'''source/database'''
	src = ET.Element('source')
	root.append(src)
	db = ET.SubElement(src, "database") 
	db.text = 'Unknown'

	'''size'''
	size = ET.Element('size')
	root.append(size)
	image = cv2.imread(os.path.join(image_path,img_name))
	_h, _w, _c = image.shape	# height, width, channel
	
	'''size/(width, heigh, depth)'''
	width = ET.SubElement(size, "width")
	width.text = str(_w)
	height = ET.SubElement(size, "height") 
	height.text = str(_h)
	depth = ET.SubElement(size, "depth") 
	depth.text = str(_c)

	'''segmented'''
	seg = ET.Element('segmented')
	root.append(seg)
	seg.text = '0'

	'''Objects'''
	for n, attribute in enumerate(data[img_name]):
		if (n+1)==len(data[img_name]):
			break
		# print("\n\n///////", labels[attribute['classId']])
		# break
		'''object'''
		obj = ET.Element('object')
		root.append(obj)

		'''name'''
		_name = ET.SubElement(obj, "name")
		label = tags[attribute['classId']]
		_name.text = label
		'''pose'''
		pose = ET.SubElement(obj, "pose") 
		pose.text = 'Unspecified'
		'''truncated'''
		truncated = ET.SubElement(obj, "truncated") 
		truncated.text = '0'
		'''difficult'''
		difficult = ET.SubElement(obj, "difficult") 
		difficult.text = '0'
		
		'''bndbox'''
		bndbox = ET.SubElement(obj, "bndbox")
		'''xmin'''
		xmin = ET.SubElement(bndbox, "xmin")
		xmin.text = str(int(attribute['points']['x1']))
		'''xmin'''
		ymin = ET.SubElement(bndbox, "ymin")
		ymin.text = str(int(attribute['points']['y1']))
		'''xmin'''
		xmax = ET.SubElement(bndbox, "xmax")
		xmax.text = str(int(attribute['points']['x2']))
		'''xmin'''
		ymax = ET.SubElement(bndbox, "ymax")
		ymax.text = str(int(attribute['points']['y2']))

	tree = ET.ElementTree(root)

	xml_file = os.path.join(annot_dir, os.path.splitext(img_name)[0]+'.xml')
	with open(xml_file, "wb") as file: 
		tree.write(file)

	'''Beautify datafile'''
	xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
	with open(xml_file, "w") as f:
	    f.write(xmlstr)


for pos in os.listdir(source_dir):
	srcfile = source_dir+'/'+pos
	print(srcfile)
	# destination
	annot_dir = os.path.join(dest_dir, 'Annotations')
	image_dir = os.path.join(dest_dir, 'JPEGImages')
	
	if not os.path.exists(annot_dir):
		os.makedirs(annot_dir)
	
	if not os.path.exists(image_dir):
		os.makedirs(image_dir)
	# source
	annotation_path = os.path.join(srcfile, 'annotations.json')
	class_path = os.path.join(srcfile, 'classes.json')
	image_path = os.path.join(srcfile, 'images')
	# print(jsonfile)	

	ap = open(annotation_path)
	annots = json.load(ap)
	
	cp = open(class_path)
	classes = json.load(cp)
	
	labels = { x['id']: x['name'] for x in classes }
	# print(labels[2])
	
	# print(json.dumps(data, indent=4, sort_keys=True))
	for image in annots:
		'''Make sure that we can read images from input directory:
					img = cv2.imread(os.path.join(image_path,image))
					cv2.imshow(image, img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()'''
		'''copy images from SuperAnnote to VOC'''
		copyfile(os.path.join(image_path,image), os.path.join(image_dir,image))
		# for attribute in annots[image]:
		# 	print(labels[attribute['classId']])	# get 'class' name assigned to the 'id'
		# 	break
		generateXML(image, annots, labels)
	



