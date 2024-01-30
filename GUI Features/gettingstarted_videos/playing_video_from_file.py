
"""
    Playing video from file is the same as capturing it from camera, just change the camera index to a video file name. 
    Also while displaying the frame, use appropriate time for cv.waitKey(). 
    If it is too less, video will be very fast and if it is too high, video will be slow. (Well, that is how we can display videos in slow motion.)
    25 miliseconds will be OK in normal cases. 
"""

import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture('spider_man.mp4')
 
while cap.isOpened():
    ret, frame = cap.read()  # ret: It is a boolean value indicating whether the frame was succesfully read or not. 

    # if frame is read correctly ret is True 
    if not ret: 
        print("Can't receive frame (stream end?). Exiting...")
        break 
    
    cv.imshow('frame', frame)

    if cv.waitKey(0) == ord('q'):
        break 

cap.release()
cv.destroyAllWindows()