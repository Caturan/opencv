"""
In this tutorial we will learn how to:
    Read an image from file (using cv::imread)
    Display an image in an OpenCv window (using cv::imshow)
    Write an image to a file (using cv::imwrite)
"""

import cv2 as cv 
import sys 

img = cv.imread("image_spiderman.jpg")

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("image_spiderman.jpg", img)

"""

Explanation:
    The OpenCV python library is imported. 
    As a first, we read the image. In order to do so, a call to the cv::imread function loads the image using the file path specified by the first argument. 
    The second argument is optional and specifies the format in which we want to image. This may be:
    - IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here. 
    - IMREAD_UNCHANGED loads the image as is. 
    - IMREAD_GRAYSCALE loads the image as an intensity one. 

    After reading the image data will be stored in a cv::Mat object. 
    img = cv.imread("image_spiderman.jpg")
        
    Afterwards, a check is executed, if the image was loaded correctly. 
    if img is None:
        sys.exit("Could not read the image")

    Then, the image is shown using a call to the cv::imshow function. 
    The first argument is the title of the window and the second argument is the cv:.Mat object that will be showns. 

    Because we want to our window to be displayed until the user presses a key (otherwise the program would end far too quickly), 
    we use the cv::waitKey function whose only parameter is just how long should it wait for a user input (measured in milliseconds). Zero means to wait forever. 

    In the end, the image is written to a file if the pressed key was the "s"-key. For this the cv::imwrite function is called that has the file path and the cv::Mat object as an argument. 

"""