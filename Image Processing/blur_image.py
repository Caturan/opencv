
"""
    As in one-dimensional signals, images also can be filtered with various low-pass filters (LFP), high-pass filters (HPF), etc. 
    LPF helps in removing noise, blurring images, etc. HPF filters help in finding edges in images. 

    OpenCV provides a function cv.filter2D() to convelve a kernel with an image. 
    As an example, we will try an averaging filter on an image. 

    The operation works like this: keep this kernel above a pixel, add all the 25 pixels below this kernel, take the average, and replace the central pixel with the new average value. 
    This operation is continued for all the pixels in the image. 
"""
import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread('OpenCV_logo.jpg')
assert img is not None, "file could not be read, chechk with os.path.exists()"

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging') 
plt.xticks([]), plt.yticks([])
plt.show()



"""
Image Blurring:
    Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. 
    It actually removes high frequency content from the image. So edges are blurred a little bit in this operation. 
    OpenCV provides four main types of blurring techniques.
"""

'''
1.Averaging:
    This done by convulving an image with a normalized box filter. It simply takes the average of all the pixels under the kernel are and replaces the central element. 
    This is done by the function cv.blur() or cv.boxFilter(). 

    If we don't want use a normalized box filter, use cv.boxFilter(). Pass an argument normalize=False to the function. 
'''

img = cv.imread('OpenCV_logo.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.blur(img,(30,30))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


'''
2.Gaussian Blurring:
    blur = cv.GaussianBlur(img,(5,5),0)
'''

'''
3.Median Blurring:
    median = cv.medianBlur(img,5)
'''

'''
4.Bilateral Filtering:
    blur = cv.bilateralFilter(img,9,75,75)
'''

