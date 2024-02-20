
"""
Goal:
    In this chapter,
        - We will learn about Image Pyramids. 
        - We will use Image pyramids to create a new fruit, "Orapple"
        - We will see these functions: cv.pyrUp(), cv.pyrDown()
"""

"""
Theory:
    Normally, we used to work with an image of constant size. But on some occasions, we need to work with (the same) images in different resolution. 
    For example, while searching for something in an image, like face, we are not sure at what size the object will be present in said image. 
    In that case, we will need to create a set of the same image with different resolutions and search for object in all of them. 
    These set of images with different resolutions are called Image Pyramids. (because when they are kept in a stack with the highest resolution image at the bottom and lowest resolution image at top, it looks like a pyramid. )          

    There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids

    Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns in Lower level (higher resolution) image. 
    Then each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian weights. 
    By doing so, M x N image becomes M/2 X N/2 image. So area reduces to one-fourth of original area. It is called an Octave. The same pattern continues as we go upper in pyramid (ie, resolution decreases). Similarly while expanding, area becomes 4 times in each level. 

    We can find Gaussian pyramids using cvçpyrDown() and cv.pyrUp() functions. 
"""

import numpy as np 
import cv2 as cv 

img = cv.imread('messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
cv.imshow('img', img)

lower_reso = cv.pyrDown(img)
cv.imshow('lower',lower_reso)


# Now we can go down the image pyramid with cv.pyrUp() function. 
higher_reso2 = cv.pyrUp(lower_reso)
cv.imshow('failed high', higher_reso2)
# Remember, higher_reso2 is not equal to higher_reso, because once we decrease the resolution, we loose the information. 
 
higher_reso = cv.pyrUp(img)
cv.imshow('higher', higher_reso)

cv.waitKey(0)
cv.destroyAllWindows()


'''
    Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. Laplacian pyramid images are like edge images only. 
    Most of its elements are zeros. They are used in image compression. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid. 
'''

