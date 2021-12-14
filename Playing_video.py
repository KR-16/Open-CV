# A video is a sequence of images/frames (called frames) captured and eventually displayed at a given frequency. However, by stopping at a specific frame of the sequence, a single video frame, i.e an image is obtained.
# A group of frames is called frameset.
# Higer the frame rate better quality/clarity in the images/video.
# Higher the frame rate calculated as FPS(Frame rate per second).
# The frame rate is the number of individual frames or images that are displayed per second of films or stills.
# Normally these frames rates are 24,30,60 fps.

import numpy as np
import cv2 as cv
capture = cv.VideoCapture("slow_motion.mp4")
while capture.isOpened(): # isOpened() is used to check whether Capture is initialized or not
   ret, frame = capture.read() # reading the frame 
   # if the frame is ready and ret is True
   # ret takes only True or None
   # if read sucessfully then ret will be True otherwise it will be None

   if not ret:
       print("Cannot reat the frame !!!. Exiting!!!!")
       break

   gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   
   cv.imshow("Frame" , gray_scale)

   width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
   height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)

   if cv.waitKey(24) == ord("q"): # pressing q will close the output window
       break
print("Width of the frame is ", width)
print("Height of the frame is ", height)
print(frame)

capture.release() # it releases the object from the memory
cv.destroyAllWindows()