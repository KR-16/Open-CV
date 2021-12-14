import numpy as np
import cv2 as cv

image = cv.imread("robo.jpg",1)
cv.imshow("Original Image",image)
print("Dimensions of original image are", image.shape)

# To downscale the image to half size
image_half = cv.resize(src = image,dsize =  (0,0)  ,  fx = 0.5, fy = 0.5)
cv.imshow("Half Size Image",image_half)

# To upscale the image to half size
image_double = cv.resize(src = image,dsize =  (0,0)  ,  fx = 2.0, fy = 2.0)
cv.imshow("Double Size Image",image_double)

# Scaling the image to a fixed size
# setting the image dimensions manually

image_fixed = cv.resize(image, (400,100))
cv.imshow("Fixed Image", image_fixed)
cv.waitKey(0)

cv.destroyAllWindows()