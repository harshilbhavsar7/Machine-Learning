import cv2
import numpy as np

def empty(a):
	pass



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",400,400)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",179,179,empty)
cv2.createTrackbar("sat min","TrackBars",73,255,empty)
cv2.createTrackbar("sat max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",70,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)


cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,400)
cap.set(10,150)
while True:
	success,img=cap.read()
	# cv2.imshow(r"Video",img)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		print("Break")
		break
	# img=cv2.imread("images/image_3.jpg")
	# img=cv2.resize(img,(400,400))
	# hor=np.hstack((img,img))
	# ver=np.vstack((img,img))
	imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	h_min=cv2.getTrackbarPos("Hue min","TrackBars")
	h_max=cv2.getTrackbarPos("Hue max","TrackBars")
	s_min=cv2.getTrackbarPos("sat min","TrackBars")
	s_max=cv2.getTrackbarPos("sat max","TrackBars")
	v_min=cv2.getTrackbarPos("val min","TrackBars")
	v_max=cv2.getTrackbarPos("val max","TrackBars")

	lower=np.array([h_min,s_min,v_min])
	upper=np.array([h_max,s_max,v_max])
	mask=cv2.inRange(imgHSV,lower,upper)
	# print(h_min)
	imageResult=cv2.bitwise_and(img,img,mask=mask)

	#Hue,saturation and value
	# cv2.imshow("image",img)
	# cv2.imshow("imageHSV",imgHSV)
	cv2.imshow("Mask",mask)
	cv2.imshow("result",imageResult)

	cv2.waitKey(1)

