import cv2
import numpy as np

img=cv2.imread("images/card.jpg")

cv2.imshow("image",img)
cv2.waitKey(0)

#points of king in the cards
up_left=[125,104]
up_right= [258,144]
down_left=[55,315]
down_right=[189,359]
width,height=250,360

points1=np.float32([up_left,up_right,down_left,down_right])
points2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(points1,points2)
imgout=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("imageout",imgout)
cv2.waitKey(0)


