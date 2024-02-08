
"""
Goal:
    - Access pixel values and modify them
    - Access image properties
    - Set a Region of Interest (ROI)
    - Split and merge images

    Almost all the operations in this section are mainly related to Numpy rather than OpenCV. 
    A good knowledge of Numpy is required to write better optimized code with OpenCV. 
"""

# Accessing and Modifying pixel values

# Let's load color image first:
import numpy as np 
import cv2 as cv 

img = cv.imread('messi.jpg')
assert img is not None, "file could not be read, check with os.path.exist()"

# We can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green, Red values. 
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

# We can modify the pixel values the same way. 
img[100,100] = [255,255,255]
print(img[100,100])

'''
Warning:
    Numpy is an optimized library for fast array calculations. So simply accessing each and every pixel value and modifying it will be very slow and its discouraged. 
'''

'''
Note:
    The above method is normally used for selecting a region of an array, say the first 5 rows and last 3 columns. 
    For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better. 
    They always return a scalar, however, so if we want to access all the B,G,R values, we will need to call array.item() seperately for each value. 
'''

# accessing RED value 
img.item(10,10,2)

# modifying RED value 
img.itemset((10,10,2),100)
img.item(10,10,2)



'''
Accessing Image Properties:
    Image properties include number of rows, columns, and channels; type of image data; number of pixels; etc. 
    The shape of an image is accessed by img.shape. It returns a tuple of the number of rows, columns, and channels (if the image is color). 
'''
print(img.shape)

# Note: If an image is grayscale, the tuple returned only the number of rows and columns, so it is a good method to check whether the loaded image is grayscale or color. 

# Total number of pixels is accessed by img.size:
print(img.size)

# Image datatype is obtained by 'img.dtype':
print(img.dtype)

cv.imshow('messi', img)
cv.waitKey(0)

'''
Image ROI:
    Sometimes, we will have to play with certain region of images. 
    For eye detection images, first face detection is done over the entire image. 
    When a face is obtained, we select the face region alone and search for eyes insideit instead of searching the whole image. 
    It improves accuracy (because eyes are always on faces :D) and performance (because we search in a small area). 
'''

# ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image:
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow('messi', img)
cv.waitKey(0)


'''
Splitting and Merging Image Channels:
    Sometimes we will need to work seperately on the B,G,R channels of an image. 
    In this case, we need to split the BGR image into single channels. 
    In other cases, we may need to join these individual channels to create a BGR image. 
'''
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

# Or
b = img[:,:,0]

# Suppose we want to set all the red pixels to zero - we do not need to split the channels first. Numpy indexing is faster. 
img[:,:,2] = 0


'''
Warning:
    cv.split() is a costly operation (in term of time). So use it only if necessary. Otherwise go for Numpy indexing. 
'''



'''
Making Borders for Images (Padding)
    If we want to create a border around an image, something like a photo frame, we can use cv.copyMakeBorder(). 
    But it has more applications for convolution operation, zero padding etc. This function takes following arguments:

    - src : input image
    - top, bottom, left, right : border width in number of pixels in corresponding directions. 
    - borderType : Flag defining what kind of border to be added. It can be following types:
        - cv.BORDER_CONSTANT : Adds a constant colored border. The value should be given as next argument. 
        - cv.BORDER_REFLECT : Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
        - cv.BORDER_REFLECT_101 or cv_BORDER_DEFAULT : Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba 
        - cv.BORDER_REPLICATE : Last element is replicated throughout, like this : aaaaaa|abcdefgh|hhhhhhh
        - cv.BORDER_WRAP : Can't explain, it will look like this: cdefgh|abcdefgh|abcdefg
    - value : Color of border if border type is cv.BORDER_CONSTANT
'''

import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

BLUE = [255,0,0]

img1 = cv.imread('OpenCV_logo.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('REFLECT_101')
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('CONSTANT')

plt.show()