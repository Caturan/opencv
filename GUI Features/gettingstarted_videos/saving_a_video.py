"""
    So we capture a video and process it frame-by-frame, and we want to save that video. 
    For images, it is very simple: just use cv.imwrite(). 

    This time we create a VideoWriter object. We should specify the output file name (eg: output.avi). 
    Then we should specify the FourCC code (details in next paragraph). 
    Then number of frames per second (fps) and frame size should be passed. 
    And the last one is the isColor flag. If it is True, the encoder expect color frame, otherwise it works with grayscale frame. 

    FourCC is 4-byte code used to specify the video codes. The list of available codes can be found in fourcc.org. It is platform dependent. 

    The below code captures from a camera, flips every frame in the vertical direction, and saves the video. 
"""

import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(0)

# Define the codec and create VideoWrite object 
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break 
    frame = cv.flip(frame, 0)

    # Write the flipped frame 
    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break 

cap.release()
out.release()
cv.destroyAllWindows()