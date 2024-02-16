
"""
Goal:
    In this tutorial, we will learn how to convert images from one color-space to another, like BGR <-> Gray, BGR <-> HSV, etc. 
    We will learn the following functions: cv.cvtColor(), cv.inRange(), etc. 
"""

"""
Changing Color-Space:
    We use the function cv.cvtColor(input_image,flag) where flag determines the type of conversion. 
    For BGR -> Gray conversion, we use the flag cv.COLOR_BGR2GRAY. Similarly for BGR -> HSV, we use the flag cv.COLOR_BGR2HSV. 
    To get other flags, just run following commands in our Python terminal:
"""
import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR')]
print(flags)


'''
Object Tracking:
    Now, that we know how to convert BGR image to HSV, we can use this to extract a colored object. 
    In HSV, it is easier to represent a color than in BGR color-space. In our application, we will try to extract a blue colored object. So here is the method:
        - Take each frame of the video 
        - Convert from BGR to HSV color-space.
        - We threshold the HSV image for a range of blue color. 
        - Now extract the blue object alone, we can do whatever we want on that image. 
'''
import numpy as np 

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()


'''
How to find HSV values to track?
    We can use the same function, cv.cvtColor(). Instead of passing an image, we just pass the BGR values we want. 
    For example, to fin the HSV value of Green:
'''
green = np.uint8([[[0,255,0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)

'''
    Now we take [H-10,100,100] and [H+10,255,255] as the lower bound respectively. 
    Apart from this method, we can use any image editing tools like GIMP or any converters to find these values, but don't forget to adjust the HSV ranges.
'''