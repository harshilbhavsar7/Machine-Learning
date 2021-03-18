import xml.etree.ElementTree as ET
import os

import cv2
# import mmcv
from PIL import Image
import numpy as np

from tqdm import tqdm

xml_root = r"D:\Infomize\AI\Annotations\entities\For_training\13-Nov\test_output\Annotations"
new_xml_root = r"D:\Infomize\AI\Annotations\entities\For_training\13-Nov\test_output\new_annot"
image_root = r"D:\Infomize\AI\Annotations\entities\For_training\13-Nov\test_output\JPEGImages"

xml_name_list = sorted(os.listdir(xml_root))


'''
It will print all the class labels in the dataset.
'''
def print_all_classes():
    all_name_list = []
    for xml_name in xml_name_list:
        print(f"{xml_name}")
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for obj in root.findall("object"):
            name = obj.find("name").text
            all_name_list.append(name)
        print(all_name_list)

'''
Check if the image size in the XML matches with the actual size of the image.
If not, then it will replace the wrong values with the correct one.
'''
def check_and_replace_hw():
    tranposed_name_lists = []
    for xml_name in xml_name_list:
        xml_path = os.path.join(xml_root, xml_name)
        print(xml_path)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        size = root.find("size")
        width = int(size.find("width").text)
        height = int(size.find("height").text)
        image_path = os.path.join(image_root, xml_name[:-4] + ".jpg")
        # print(image_path,xml_name)
        img = cv2.imread(image_path, flags=cv2.IMREAD_COLOR)
        h, w, _ = img.shape
        if height != h or width != w:
            print(width, w, height, h)
            print(f"{xml_name}'s h, w is tranposed.")
            tranposed_name_lists.append(xml_name)
            # If height and width not match, change it to its correct values
            tree.find('size/width').text = w
            tree.find('size/height').text = h
            tree.write(xml_path)

    print(tranposed_name_lists)

'''
1. Switch x1 with x2 & y1 with y2 if xmin and ymin are greater than xmax and ymax.
2. decrease xmax and ymax to the image's height and width is the former is larger than the image itself.
'''
def check_bbox():
    if not os.path.exists(new_xml_root):
        os.makedirs(new_xml_root)

    for xml_name in tqdm(xml_name_list):
       
        xml_path = os.path.join(xml_root, xml_name)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for obj in root.findall("object"):
            bnd_box = obj.find("bndbox")
            coords = [int(float(bnd_box.find('xmin').text)), int(float(bnd_box.find('ymin').text)), int(float(bnd_box.find('xmax').text)), int(float(bnd_box.find('ymax').text))]

            if coords[0] >= coords[2]:
                bnd_box.find('xmax').text = coords[0]
                bnd_box.find('xmin').text = coords[2]

            if coords[1] >= coords[3]:
                bnd_box.find('ymax').text = coords[1]
                bnd_box.find('ymin').text = coords[3]

            image_path = os.path.join(image_root, xml_name[:-4] + ".jpg")
            # print(image_path,xml_name)
            img = cv2.imread(image_path, flags=cv2.IMREAD_COLOR)
            # print(image_path,xml_name)
            h, w, _ = img.shape

            if coords[3] > h or coords[2] > w:
                bnd_box.find("xmax").text = str(min(w, coords[2]))
                bnd_box.find("ymax").text = str(min(h, coords[3]))
                # root.remove(obj)  # We can also remove the object if necessary.
        tree.write(xml_path)
        tree.write(os.path.join(new_xml_root, xml_name))

check_and_replace_hw()
check_bbox()
print('done')