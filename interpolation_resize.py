import cv2 as cv
import numpy as np

image = cv.imread("Red-Rose.jpg",cv.IMREAD_COLOR)

cv.imshow("Original Image",image)

image_1 = cv.resize(image,(1000,1000),interpolation = cv.INTER_AREA)
cv.imshow("INTER AREA IMAGE",image_1)

image_2 = cv.resize(image,(1000,1000),interpolation = cv.INTER_LINEAR)
cv.imshow("INTER LINEAR IMAGE",image_2)

image_3 = cv.resize(image,(1000,1000),interpolation = cv.INTER_NEAREST)
cv.imshow("INTER NEAREST IMAGE",image_3)

image_4 = cv.resize(image,(1000,1000), interpolation = cv.INTER_CUBIC)
cv.imshow("INTER CUBIC IMAGE",image_4)

cv.waitKey(0)