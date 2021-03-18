import cv2
import numpy as np

def getContours(img):
	contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		area=cv2.contourArea(cnt)
		print(area)
		if  area>50:
			cv2.drawContours(imgcopy,cnt,-1,(0,0,255),3)
			peri=cv2.arcLength(cnt,True)
			approx=cv2.approxPolyDP(cnt,0.02*peri,True)
			print(len(approx))
			objCor=len(approx)

			if objCor==4 :
				aspratio=w/float(h)
				if aspratio>0.95 and aspratio<1.05:objectType="Square"
				else:objectType="rectangle"
			elif objCor>4 :objectType="Circle"

			x,y,w,h=cv2.boundingRect(approx)
			cv2.rectangle(imgcopy,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(imgcopy,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,0),2)

path="images/image_5.jpg"

img=cv2.imread(path)
imgcopy=img.copy()

imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),1)
imgCanny=cv2.Canny(imgblur,50,50)


imggraybgr=cv2.cvtColor(imggray,cv2.COLOR_GRAY2BGR) 
imgblurbgr=cv2.cvtColor(imgblur,cv2.COLOR_GRAY2BGR)
imgCannybgr=cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
getContours(imgCanny)
imgblank=np.zeros_like(img)
imgh1stack=np.hstack((imgblurbgr,imgblurbgr))
imgh2stack=np.hstack((imgCannybgr,imgcopy))
imgvstack=np.vstack((imgh1stack,imgh2stack))
cv2.imshow("image",imgvstack)
# cv2.imshow("image2",imggray)
# cv2.imshow("image3",imgblur)
# cv2.imshow("image4",imgCanny)
getContours(imgCanny)
cv2.waitKey(0)