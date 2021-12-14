from rotation import Matrix_2
import numpy as np
import cv2 as cv

original_image = cv.imread("Mickey_mouse.jpg",cv.IMREAD_COLOR)
cv.imshow("Original original_image",original_image)

#Dimensions
height,width,channel = original_image.shape

# Transformation Matrix
# The original_image is scaled to half of it's size
matrix_1 = cv.getRotationMatrix2D(center = (255,255), angle = -45, scale = 0.5)
# Rotation
rotate_1 = cv.warpAffine(src = original_image , M = matrix_1, dsize = (width,height))
cv.imshow("Rotated by -45 degree",rotate_1)

# Transformation Matrix
# The original_image is doubled to it's size
matrix_2 = cv.getRotationMatrix2D(center = (100,100), angle = -180, scale = 2.0)
# Rotation
rotate_2 = cv.warpAffine(src  = original_image , M = matrix_2, dsize = (400,400))
cv.imshow("Rotated original_image bu -180 degree",rotate_2)

cv.waitKey(0)