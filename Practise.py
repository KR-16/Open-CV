import numpy as np
import cv2
img1 = np.zeros((400,400,3), np.uint8)
cv2.rectangle(img1,(20,20),(100,150),(0,255,255),-1)
cv2.imshow("Image",img1)
r,c,ch = img1.shape
print(r,c,ch)
cv2.waitKey(0)