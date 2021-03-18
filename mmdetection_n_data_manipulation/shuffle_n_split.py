'''
This script is used to split the data into training and test dataset used for Machine learning applications.
Two files will be generated after executing the script. These are train.txt and test.txt for their respective data.

Used to split Pascal VOC dataset.
Made_by : Tarun Mahajan
'''


from os import listdir
import argparse
import os
import random

parser = argparse.ArgumentParser()
parser.add_argument("--directory", '-d', type=str, help="Provide VOC folder path")
parser.add_argument("--split_ratio", '-sr', type=float, help="split ratio. E.g. '0.8' for 80% split")
args = parser.parse_args()


dir_path = args.directory
data_dir = os.path.join(dir_path, "Annotations")
image_dir = os.path.join(dir_path, "JPEGImages")

main_dir =  os.path.join(dir_path, "Main")
if not os.path.exists(main_dir):
    os.makedirs(main_dir)

split_ratio = args.split_ratio

def splitdata(filelist, split_ratio):
	arr1 = []
	arr2 = []
	size = len(filelist)
	split_size = int(size*split_ratio)
	i=0
	for file in filelist:
		if i <= int(split_size):
			arr1.append(file)
		else:
			arr2.append(file)
			# print(os.path.splitext(file)[0])
		i+=1
		'''Check if the corresponding image exist or not. If not then remove the filename from the list'''
		img_path = os.path.join(image_dir, file+".jpg")
		if not os.path.exists(img_path):
			raise Exception("File image does not exist!")
	return arr1, arr2

def write2txt(txtpath, filelist):
	txt = open(txtpath, "w")
	txt.truncate(0)
	for file in filelist:
		txt.write(file+"\n")
		# print(file)
	txt.close()

	f = open(txtpath, "r")
	print(f.read())
	f.close()

filelist = []
for file in listdir(data_dir):
	filename = os.path.splitext(file)[0]
	img_path = os.path.join(image_dir, filename+".jpg")
	if os.path.exists(img_path):
		filelist.append(filename)
	else:
		print('\n***Caution: Image doesnot exist!***')
		print(file)

random.shuffle(filelist)

trainval, test = splitdata(filelist, 0.8)
train, val = splitdata(trainval, 0.8)

write2txt(os.path.join(main_dir, "train.txt"), train)
write2txt(os.path.join(main_dir, "test.txt"), test)
write2txt(os.path.join(main_dir, "val.txt"), val)

print("Successfull")

print('total length', len(filelist))
print('train', len(train))
print('val', len(val))
print('test', len(test))

# print('train', train)
# print('\n')
# print('val', val)
# print('\n')
# print('test', test)
