"""
Goal:
    - Learn to draw different geometric shapes with OpenCV 
    - We will learn these functions
"""

"""
Code: 
    In all the above functions, we will see some common arguments as given below:
    - img: The image where we want to draw the shapes
    - color: Color of the shape. for BGR, pass it as a tuple, eg(255,0,0) for blue. For grayscale, just pass the scalar value. 
    - thickness: Thickness of the line or circle etc. If -1 passed for closed figures like circles, it will fill the shape. default thickness = 1 
    - lineType: Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves. 
"""

"""
Drawing Line:
    To draw a line, we need to pass starting and ending coordinates of line. 
    We will create a black image and draw a blue line on it from top-lef to bottom-right corners. 
"""

import numpy as np 
import cv2 as cv 

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Drawing Line
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.imshow('imgLine', img)
cv.waitKey(0)


# Drawing Rectangle
# To draw a rectangle, we need top-left corner and bottom-right corner of rectangle. This time we will draw a green recgtangle at the top-right corner of image.
cv.rectangle(img,(384,0),(510,128),(0,0,255),2)
cv.imshow('imgLine', img)
cv.waitKey(0)


# Drawing Circle
# To draw a circle, we need its center coordinates and radius. We will draw a circle inside the rectangle drawn above. 
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.imshow('imgLine', img)
cv.waitKey(0)


# Drawing Ellipse
"""
    To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). 
    Next argument is axes lengths. Angle is the angle of rotation of ellipse in anti-clockwise direction. 
"""
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv.imshow('imgLine', img)
cv.waitKey(0)


# Drawing Polygon
"""
    To draw a polygon, first we need coordinates of vertices. 
    Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32. 
"""
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
cv.imshow('imgLine', img)
cv.waitKey(0)

"""
Note:
    If third argument is False, we will get a polylines all the points, not a closed shape. 
    cv.polylines() can be used to draw multiple lines. Just create a list of all the lines we want to draw and pass it to the function. 
     All lines will be drawn individually. It is a much better and faster way to draw a group of lines than calling cv.line() for each line. 
"""


"""
Adding Text to Images:
    - Text data that we want to write
    - Position coordinates of where we want put it 
    - Font type (Check cv.putText() docs for supported fonts)
    - Font Scale (specifies the size of font)
    - regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended. 
"""

# We will write OpenCV on our image in white color. 
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'CAT',(10,500),font,4,(255,255,255),2,cv.LINE_AA)
cv.imshow('imgLine', img)
cv.waitKey(0)