'''
Image preprocessing to improve training speed and model accuracy:
	1. Convert RGB image to Grayscale image
	2. Convert Grayscale image to Binary image

Explained:
	1. A binary image has only two values for each pixel, 0 and 1 corresponding to black and white (or vice versa).
	2. A gray scale image has a certain number (probably 8) bits of information per pixel, hence, 256 possible grey values.
'''

'''
Reference link for Image preprocessing in deep learning:
	1. https://stackoverflow.com/questions/41428868/image-preprocessing-in-deep-learning
'''




import cv2
import os
from os import listdir
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--source", '-s', type=str, help="Provide the path of source directory")
parser.add_argument("--destination", '-d', type=str, help="Provide the path of destination directory")
args = parser.parse_args()

image_dir = args.source
dest_dir = args.destination
# defect=[]

'''
This is a Dimentionality reduction technique, which allows the neural network's performance to be invariant to that dimension, or to make the training problem more tractable.
'''
def RGB2GreyScale():
	# dest_path = os.path.join(dest_dir, 'Greyscale')

	# if not os.path.exists(dest_path):
	# 	os.makedirs(dest_path)
	for file in listdir(image_dir):
		print(file)
		image = cv2.imread(os.path.join(image_dir, file))
		# _image = cv2.resize(image, (900, 1200)) 
		# cv2.imshow('Original', _image)
	
		# We use cvtColor, to convert to grayscale 
		gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
		# gray_img = cv2.resize(gray_image, (900, 1200)) 
		# cv2.imshow('Grayscale', gray_img)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()

		# print(image.shape)
		# print(gray_image.shape)
		# print('Original (RGB):', image[200, 550])
		# print('Greyscale:', gray_image[200, 550])

		# Write grayscale image to destination directory
		new_file_path = os.path.splitext(file)[0]+os.path.splitext(file)[1]
		cv2.imwrite(os.path.join(dest_dir, new_file_path), gray_image)

'''
While converting a gray scale image to a binary image, we usually use cv2.threshold() and set a threshold value manually. Sometimes to get a decent result we opt for Otsu's binarization.

'''
def RGB2Binary():
	# dest_path = os.path.join(dest_dir, 'Binary')

	# if not os.path.exists(dest_path):
	# 	os.makedirs(dest_path)
	for file in listdir(image_dir):
		# print(file)
		
		# 1. Read a grayscale image
		im_gray = cv2.imread(os.path.join(image_dir, file), cv2.IMREAD_GRAYSCALE)
		# _gray = cv2.resize(im_gray, (900, 1200)) 
		# cv2.imshow('Grayscale', _gray)

		# 2. Convert grayscale image to binary
		(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
		# The above code determines the threshold automatically from the image using Otsu's method

		# _bw = cv2.resize(im_bw, (900, 1200)) 
		# cv2.imshow('Binary', _bw)
		# cv2.waitKey(0)

		# print('Greyscale:', im_gray[200, 550])
		# print('Binary:', im_bw[200, 550])

		# Write binary image to destination directory
		new_file_path = os.path.splitext(file)[0]+"_Binary"+os.path.splitext(file)[1]
		cv2.imwrite(os.path.join(dest_dir, new_file_path), im_bw)


 
RGB2GreyScale()
# RGB2Binary()
# print(defect)


