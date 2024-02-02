
"""
More Advanced Demo:
    Now we go for a much better application. In this, we draw either rectangles or circles (depending on the mode we select) by dragging the mouse like we do in Paint application. 
    So our mouse callback funciton has two parts, one to draw rectangle and other to draw the circles. 
    This specific example will be really helpful in creating and understanding some interactive applications like object tracking, image segmentation etc. 
"""
import numpy as np 
import cv2 as cv 

drawing = False # true if mouse is pressed 
mode = True 
ix, iy = -1, -1 

# mouse callback function 
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode 

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True 
        ix, iy = x, y 

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix, iy),(x,y),(255,0,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False 
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)


# In the main loop, we should set a keyboard binding for key 'm' to toggle between rectangle and circle. 
if __name__ == "__main__":
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    
    while(1):
        cv.imshow('image', img),
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):  # ascii code of m(77)
            mode = not mode 
        elif k == 27:
            break 

    cv.destroyAllWindows()