import cv2 as cv
import numpy as np
house = cv.imread("house.jpg",cv.IMREAD_COLOR)
background = cv.imread("background.jpg",cv.IMREAD_COLOR)

# I want to put the house imge in the top-left corner 
rows, cols, channels = house.shape

# Collecting the portion/region of water image which is in the house image
background_resize = background[0:rows,0:cols]

# Now creating a mask(thresholder) for the house image
ret, house_thresh = cv.threshold(src = house,thresh = 20,maxval= 255,type = cv.THRESH_BINARY)

# the below statement can also be obtained by giving the type as cv.THRESH_BINARY_INV
house_thresh_inverse = cv.bitwise_not(house_thresh)


# Now Black-out the area of the House in the background_resize
background_image = cv.bitwise_and(background_resize,background_resize,mask = house_thresh_inverse)
cv.imshow("BACKGROUND IMAGE", background_image)

cv.waitKey(0)