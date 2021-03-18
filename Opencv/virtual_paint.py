import cv2
import numpy as np

mycolors=[0,183,160,179,255,216]
mycolorsvalue=[[0,0,255]]

myPoints=[]

def findcolour(img,mycolors,mycolorsvalue):
	imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	newPoints=[]
	lower=np.array(mycolors[0:3])
	# print(lower)
	upper=np.array(mycolors[3:6])
	# print(upper)
	mask=cv2.inRange(imgHSV,lower,upper)
	x,y,w,h=getContours(mask)
	if x:
		# cv2.rectangle(imgResult,(x,y),(x+w,y+h),mycolorsvalue[0],cv2.FILLED)
		cv2.circle(imgResult,(x,y),10,mycolorsvalue[0],cv2.FILLED)
		newPoints.append([x,y,w,h])

	return newPoints
	# cv2.imshow("mask",mask)


def drawonCanvas(myPoints,mycolorsvalue):
	for points in myPoints:
		cv2.circle(imgResult,(points[0],points[1]),10,mycolorsvalue[0],cv2.FILLED)
		# cv2.rectangle(imgResult,(points[0],points[1]),(points[0]+points[2],points[1]+points[3]),mycolorsvalue[0],cv2.FILLED)


def getContours(img):
	x,y,w,h=0,0,0,0
	contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		area=cv2.contourArea(cnt)
		# print(area)
		if  area>50:
			cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
			peri=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt,0.02*peri,True)
			# print(len(approx))
			objCor=len(approx)
			x,y,w,h=cv2.boundingRect(approx)
	return x+w//2,y,w,h

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
while True:
	success,img=cap.read()
	imgResult=img.copy()
	newPoints= findcolour(img,mycolors,mycolorsvalue)
	if len(newPoints)!=0:
		for newP in newPoints:
			myPoints.append(newP)
	if len(myPoints)!=0:
		drawonCanvas(myPoints,mycolorsvalue)
	cv2.imshow(r"Result",imgResult)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		print("Break")
		break