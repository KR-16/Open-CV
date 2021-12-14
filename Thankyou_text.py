import numpy as np
import cv2
import emoji
font = cv2.FONT_HERSHEY_TRIPLEX
# Create a black image
img = np.zeros((512,512,3), np.uint8)
tick=str(emoji.emojize(':heavy_check_mark:'))
cv2.putText(img,tick,'THANK YOU',(75,256), font, 2,(255,255,255),2)
#Display the image
cv2.imshow("img",img)

cv2.waitKey(0)