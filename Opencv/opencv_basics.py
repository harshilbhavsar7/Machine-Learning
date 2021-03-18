import cv2
import numpy as np


kernal=np.ones((5,5),np.uint8)
#reading and showing the image 

# img= cv2.imread(r"images/image_1.jpg")
# cv2.imshow(r"image",img)
# cv2.waitKey(0)

#reading and showing video file

# cap = cv2.VideoCapture(r"videos/video_1.mp4")
# while True:
# 	success,img=cap.read()
# 	cv2.imshow(r"Video",img)
# 	if cv2.waitKey(1) & 0xFF==ord('q'):
# 		print("Break")
# 		break

# Webcam interaction

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,10000)
# while True:
# 	success,img=cap.read()
# 	cv2.imshow(r"Video",img)
# 	if cv2.waitKey(1) & 0xFF==ord('q'):
# 		print("Break")
# 		break


img= cv2.imread(r"images/image_2.jpg")

#convering to grayscale
image2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("ImageGray",image2)
cv2.waitKey(0)

#blurring the iamge
imageblur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("ImageBlur",imageblur)
cv2.waitKey(0)

#canny edge detector
imagecanny=cv2.Canny(img,250,250)#the two numbers are threshold vlaues
cv2.imshow("ImageCanny",imagecanny)
cv2.waitKey(0)

#hard edges 
imgDilation=cv2.dilate(imagecanny,kernal,iterations=1)
cv2.imshow("Imagedilate",imgDilation)
cv2.waitKey(0)

#thinner edges 
imgEroded=cv2.erode(imgDilation,kernal,iterations=1)
cv2.imshow("Imageeroded",imgEroded)
cv2.waitKey(0)

