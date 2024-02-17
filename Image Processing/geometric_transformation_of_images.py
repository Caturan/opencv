
"""
Goals:
    - Learn to apply different geometric transfarmations to images, like translation, rotation, affine transformatio etc. 
    - We will see these functions: cv.getPerspectivfeTransform
"""

"""
Transformations:
    OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, with which we can perform all kinds of transformations. 
    cv.warpAffine takes a 2x3 transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix as input. 
"""

"""
Scaling:
    Scaling is just resizing of the image. OpenCV comes with a function cv.resize() for this purpose. 
    The size of the image can be specified manually, or we can specify the scaling factor. Different interpolation methods are used. 
    Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming. 
    By default, the interpolation method cv._INTER_LINEAR is used for all resizing purposes. We can resize an input image with either of following methods:
"""

import numpy as np 
import cv2 as cv

img = cv.imread('messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

res = cv.resize(img,None,fx=2, fy=2, interpolation= cv.INTER_CUBIC)

# or

height, width = img.shape[:2]
res = cv.resize(img,(2*width,2*height), interpolation=cv.INTER_CUBIC)

cv.imshow('img', img)
cv.waitKey(0)
cv.imshow('resize', res)
cv.waitKey(0)


'''
Translation:
    Translation is the shifting of an object's location. If we know the shift in the (x,y) direction and let it be (tx,ty), we can create the transformation matrix. 
    
    We can make it into a Numpy array of type np.float32 and pass it into the cv.warpAffine() function. See the below example for a shift of (100,50):
'''

import numpy as np 
import cv2 as cv 

img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('shifted',dst)
cv.waitKey(0)
cv.destroyAllWindows()


'''
Rotation:
    Rotation of an image for an angle is achieved by the transformation matrix of the form. 
    But OpenCV provides scaled rotation with adjustable center of rotation so that we can rotate at any location we prefer. 

    The find the transformation matrix, OpenCV provides a function, cv.getRotationMatrix2D. Check out the below example which rotates the image by 90 degree with respect to center without any scaling. 
'''

img = cv.imread('messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
#rows,cols = img.shape

# cols-1 and rows-1 are the coordinate limits. 
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('rotate',dst)
cv.waitKey(0)



'''
Affine Transformation:
    In affine transformation, all parallel lines in the original image will still be parallel in the output image. 
    The cv.getAffineTransform will create a 2x3 matrix which is to be passed to cv.warpAffine. 
'''
from matplotlib import pyplot as plt 

img = cv.imread('drawing.png')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv.getAffineTransform(pts1,pts2)

dst = cv.warpAffine(img,M,(cols,rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()



'''
Perspective Transformation: 
    For perspective transformation, we need a 3x3 transformation matrix. Straight lines will remain straight even after the transformation. 
    To find this transformation matrix, we need 4 points on the input image and corresponding points on the output image. 
    Then the transformation matrix can be found by the function cv.getPerspectiveTransform. Then apply cv.warpPerspective with this 3x3 transformation matrix.
'''
img = cv.imread('sudoku.png')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img,M,(300,300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()