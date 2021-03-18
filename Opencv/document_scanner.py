import cv2
import numpy as np

kernal=np.ones((5,5),np.uint8)

width,height=800,600
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
cap.set(10,150)


def preprocessing(img):
	image2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	imageblur=cv2.GaussianBlur(img,(5,5),1)
	imagecanny=cv2.Canny(imageblur,250,250)
	imgDilation=cv2.dilate(imagecanny,kernal,iterations=2)
	imgThresh=cv2.erode(imgDilation,kernal,iterations=1)
	return imgThresh

def reorder(myPoints):
	myPoints=myPoints.reshape((4,2))
	mypointsNew=np.zeros((4,1,2),np.int32)
	add=myPoints.sum(1)
	mypointsNew[0]=myPoints[np.argmin(add)]
	mypointsNew[3]=myPoints[np.argmax(add)]
	diff=np.diff(myPoints,axis=1)
	mypointsNew[1]=myPoints[np.argmin(diff)]
	mypointsNew[2]=myPoints[np.argmax(diff)]
	return mypointsNew

def getwarp(img,biggest):
	biggest= reorder(biggest)

	points1=np.float32(biggest)
	points2=np.float32([[0,0],[width,0],[0,height],[width,height]])
	
	matrix=cv2.getPerspectiveTransform(points1,points2)
	imgout=cv2.warpPerspective(img,matrix,(width,height))

	return imgout


def getContours(img):
	biggest=np.array([])
	Maxarea=0
	contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		area=cv2.contourArea(cnt)
		if  area>2500:
			# cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
			peri=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt,0.02*peri,True)
			if len(approx)==4 and area>Maxarea:
				biggest=approx
				Maxarea=area
	cv2.drawContours(imgResult,biggest,-1,(255,0,0),20)
	return biggest			

while True:
	success,img=cap.read()
	imgResult=img.copy()
	imgThresh=preprocessing(img)
	biggest=getContours(imgThresh)
	# print(biggest)
	cv2.imshow(r"Video",imgResult)
	if biggest.size !=0:
		imgWarped=getwarp(img,biggest)
		# if imgWarped:
		cv2.imshow(r"warp",imgWarped)
	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		print("Break")
		break