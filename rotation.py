import numpy as np
import cv2 as cv

image = cv.imread("boy.jpg",cv.IMREAD_COLOR)
cv.imshow("Original Image",image)

# Dimensions of the image and calculate the centre if the image

# width = across x-axis
#height = across y-axis
height,width,channels = image.shape
center_x, center_y = (width/2,height/2)

# Transformation Matrix
Matrix_1 = cv.getRotationMatrix2D(center = (center_x,center_y),angle = 45,scale = 1.0)
# scale = 1.0 the original image will not resize
# scale = 0.5 original image will decreased by half of the size
# scale = 2.0 the original image will be doubled by it's size

#Rotating the image
rotate_1 = cv.warpAffine(src = image, M = Matrix_1, dsize = (width,height))
cv.imshow("Rotated image by 45 degree",rotate_1)

# Transform Matrix
Matrix_2 = cv.getRotationMatrix2D(center = (center_x,center_y), angle = (-90), scale = 1.0)
rotate_2 = cv.warpAffine(src = image, M = Matrix_2,dsize = (width,height))
cv.imshow("Image rotated by -90 degree",rotate_2)

cv.waitKey(0)