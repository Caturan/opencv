import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting..")
        break

    blur = cv.blur(frame,(10,10))

    cv.imshow('frame', blur)

    if cv.waitKey(1) == ord('q'):
        break 

cap.release()
cv.destroyAllWindows()