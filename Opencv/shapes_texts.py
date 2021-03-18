import cv2
import numpy as np

img=np.zeros((514,514,3),np.uint8)


# img[:]=255,0,0
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),4)
# cv2.rectangle(img,(100,100),(200,200),(0,255,0),4)
# cv2.rectangle(img,(100,100),(200,200),(0,255,0),cv2.FILLED)
# cv2.circle(img,(250,250),50,(0,0,255),4)
# cv2.circle(img,(250,250),50,(0,255,255),cv2.FILLED)
cv2.putText(img,"Opencv",(250,250),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),4)# 1 is scale

cv2.imshow("Image",img)
cv2.waitKey(0)	