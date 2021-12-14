import cv2 as cv
import numpy as np

image = cv.imread("boy.jpg",cv.IMREAD_COLOR) # we can even read it in grayscale image also
#image is the cv::mat object of the image

# COVERTING THE IMAGE TO GRAY SCLAE USING cvtColor method
gray_scale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("Original Image",image)
cv.imshow("Gray Scale Image",gray_scale)

# RESIZING THE IMAGE
gray = cv.resize(gray_scale,(200,200)) 
cv.imshow("RESIZED GRAY IMAGE",gray)

ret,thresh_1 = cv.threshold(src = gray,thresh=100, maxval= 255, type = cv.THRESH_BINARY)
ret,thresh_2 = cv.threshold(src = gray,thresh=90,maxval=255,type=cv.THRESH_BINARY_INV)
ret,thresh_3 = cv.threshold(src = gray,thresh=90,maxval=255,type=cv.THRESH_TRUNC)
ret,thresh_4 = cv.threshold(src = gray,thresh=90,maxval=255,type=cv.THRESH_TOZERO)
ret,thresh_5 = cv.threshold(src = gray,thresh=90,maxval=255,type=cv.THRESH_TOZERO_INV)

print(ret)
cv.imshow("Thresh Binary Image",thresh_1)
cv.imshow("Thresh Binary Inverted Image",thresh_2)
cv.imshow("Thresh Truncated Image",thresh_3)
cv.imshow("Thresh TOZERO Image",thresh_4)
cv.imshow("Thresh TOZERO INVERSE Image",thresh_5)
cv.waitKey(0)
