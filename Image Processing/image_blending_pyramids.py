
"""
Image Blending using Pyramids:
    One application of Pyramids is Image Blending. For example, in image stitching, we will need to stack two images together, but it may not look good due to discontinuities between images. 
    In that case, image blending with Pyramids gives us seamless blending without leaving much data in the images. 
    One classical example of this is the blending of two furits, Orange and Apple. See the result now itself to understand what I am saying:
"""

"""
Please check first reference in additional resources, it has full diagramatic details on image blending, Laplacian Pyramids etc. Simply it is done as follows:
    1. Load the two images of apple and orange. 
    2. Find the Gaussian Pyramids for apple and orange. 
    3. From Gaussian Pyramids, find their Laplacian Pyramids. 
    5. Finally from this joint image pyramids, reconstruct the original image. 
"""

import cv2 as cv 
import numpy as np,sys

A = cv.imread('apple.jpg')
B = cv.imread('orange.jpg')
assert A is not None, "file could not be read, check with os.path.exists()"
assert B is not None, "file could not be read, check with os.path.exists()"

# generate Gaussian pyramid for A 
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B 
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A 
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B 
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)

# now add left and right halves of images in each level 
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_,LS[i])

# image with direct connecting each half
real = np.stack((A[:,:cols//2],B[:,cols//2:]))

# image with direct connecting each half 
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

cv.imwrite('Pyramid_blending2.jpg',ls_)
cv.imwrite('Direct_blending.jpg',real)
