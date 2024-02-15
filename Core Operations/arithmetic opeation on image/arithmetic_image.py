
"""
Goal:
    - Learn several arithmetic operations on images, like addition, substraction, bitwise operations, and etc.
    - Leanr these functions: cv.add(), cv.addWeighted(), etc 
"""

'''
Image Addition:
    We can add two images with the OpenCV function, cv.add(), or simply by the numpy operation res = img1 + img2. 
    Both images should be of same depth and type, or the second image can just be a scalar value. 
'''
import numpy as np
import cv2 as cv

x = np.uint8([250]) # 250+10 = 260 => 255
y = np.uint8([10])  # 250 + 10 = 260 % 256 = 4

print(cv.add(x,y))

print(x+y)
# This will be more visible when we add two images. Stick with OpenCV functions, because they will provide a better result. 


"""
Image Blending:
    This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency. Images are added as per the equation below:
        g(x) = (1-a)f0(x) + af1(x)
    By varying a from 0 -> 1, we can perform a cool transition between one image to another. 

    Here we took two images to blend together. The first image a weight of 0.7 and the second image is given 0.3 cv.addWeighted() applies the following equation to the image:
        dst = a.img1 + ß.img2 + y 
    Here y is taken as zero. 
"""

img1 = cv.imread('ml.png')
img2 = cv.imread('OpenCV_logo.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"

dst = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow('dst',dst) # we can take error in there we should be sure size of the images.
cv.waitKey(0) 
cv.destroyAllWindows()


"""
Btiwise Operations:
    This includes the bitwise AND, OR, NOT, and XOR operations. They will be highly useful while extracting any part of the image, defining and working with non-rectangular ROI's, and etc. 
    Below we will see an example of how to change a particular region of an image. 

    I want to put the OpenCV logo above an image. If i add two images, it will change the color. If i blend them, i get a transparent effect. But i want to be opaque. 
    If it was a rectangular region, i could use ROI as we did in the last chapter. But the OpenCV logo is a not rectangular shape. So we can do it bitwise operation as shown below:
"""
# Load two images 
img1 = cv.imread('messi.jpg')
img2 = cv.imread('OpenCV_logo.jpg')
assert img1 is not None, "file couldnt not be read, check with os.path.exists()"
assert img2 is not None, "file couldnt not be read check with os.path.exists()"

# I want to put logo on top-lef corner, so i craete a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also 
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()