import cv2 as cv
import numpy as np

image = cv.imread("house.jpg",cv.IMREAD_COLOR)
cv.imshow("ORIGINAL IMAGE",image)
width,height,channel = image.shape

print("Width:",width)
print("Height:",height)
print("Channels:",channel)

Matrix_1 = np.float32([[1,0,100],[0,1,50]])
dst_1 = cv.warpAffine(image,M = Matrix_1,dsize = (height,width))
cv.imshow("Translated Image 100 pixels towards the right and 50 pixels down",dst_1)

Matrix_2 = np.float32([[1,0,-100],[0,1,-50]])
dst_2 = cv.warpAffine(image,M = Matrix_2,dsize = (height,width))
cv.imshow("Translated Image 100 pixes towards the left and 50 pixels above",dst_2)


cv.waitKey(0)