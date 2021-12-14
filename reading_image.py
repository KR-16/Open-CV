# import the modules
import cv2 as cv
import sys
import numpy as np

# imread is used to read the image
image = cv.imread("birds.jpg",cv.IMREAD_GRAYSCALE)
# reads the image in GrayScale
if image is None:
    sys.exit("The image is not found in the specified path!!!! :(( ")
print("The shape of the image: ",end = " ")
height ,weight  = image.shape # shape attribute
print("height = ",height, " weight = ",weight)
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(image, "V Y KEERTHI RAJ",(10,30),font, 0.6, (255,255,255),1, cv.LINE_AA)

cv.imshow("Reading the image ", image)

# waitKey is used for wait time in the output screen
# 0 represents for infinte wait time
k = cv.waitKey(0)
# k is returned by the unicode function from the waitKey()
print("To save the image file type 's' , other wise press any other key to exit")
if k == ord("s"):
# if the key pressed by the image by the user is "s" then the image will be saved
    cv.imwrite("birds_grayscale.jpg",image)