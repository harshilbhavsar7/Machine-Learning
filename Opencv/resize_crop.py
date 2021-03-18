import cv2
import numpy as np

img= cv2.imread(r"images/image_1.jpg")
# print(img.shape)# output=(2160, 3840, 3) where this is in height,width,channels  

imgresize=cv2.resize(img,(640,480))#here width comes first then height (width,height)

imgcropped=imgresize[0:200,200:500]# here height comes first then width(height,width0)

cv2.imshow(r"image resize",imgresize)
cv2.imshow(r"image crop",imgcropped)#try overlapping this one with the main one to see from where it has been crope

cv2.waitKey(0)