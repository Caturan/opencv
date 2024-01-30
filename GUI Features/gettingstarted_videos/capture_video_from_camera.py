"""
    Often, we have to capture live stream with a camera. OpenCV provides a very simple interface to do this. 
    Let's capture a video from the camera, convert it into grayscale video and display it. 

    To capture a video, we need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. 
    A device index is just the number to specify which camera. 
    Normally one camera will be connected. So simply pass 0 or (-1). 
    We can select the second camera by passing 1 and so on.
    After that, we can capture frame-by-frame. But at the end, don't forget to release the capture.  
"""

import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1080) 
cap.set(cv.CAP_PROP_FRAME_HEIGHT,840)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()     # ret: It is a boolean value indicating whether the frame was succesfully read or not. 

    # if frame is read correctly ret is True 
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break 

    # Operation on the frame come here 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame 
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture 
cap.release()
cv.destroyAllWindows()

"""
    cap.read() returns a bool. 
    We can check whether it is initialized or not by the method cap.isOpened(). Otherwise open it using cap.open(). 

    We can also access some of the features of this video using cap.get(propId) method where propId is a number from 0 to 18. 
    Some of these values can be modified using cap.set(propID, value). 

    For example, we can check the frame width and height by cap.get(cv.CAP_PROP_FRAME_WIDTH) and cap.get(cv.CAP_PROP_FRAME_HEIGHT). It gives us 640x480 by default. 
    But we want to modify it to 320x240. Just use ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

"""
