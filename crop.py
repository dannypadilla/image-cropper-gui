'''
This program provides something.... 
* 1. draw a box around a region-of-interest (ROI) to crop
* 2. roi is stored to disk (./cropped/)

Usage:
crop.py [<some_args>, here]

Output:
 Stores a cropped ROI to ./cropped/
'''
import cv2
import numpy as np
import os, sys
from subprocess import check_output

drawing = False # true if mouse is pressed
ix, iy = -1, -1


# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, roi
    img_cpy = param.copy()
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        ix, iy = x, y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if drawing == True:
            #cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.rectangle(img_cpy, (ix, iy), (x, y), (0, 255, 0), 1)
    elif (event == cv2.EVENT_LBUTTONUP):
        drawing = False
        roi = (ix, iy, x, y)
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)


if __name__ == "__main__":

    clear_screen_cmd = check_output(["clear", "."]).decode("utf8")
    print(clear_screen_cmd) # clears terminal (ctrl + l)

    print(__doc__)

    try:
        img_path = sys.argv[1]
    except:
        img_path = "../images/front10.jpg"
        #img_path = "../images/front98.jpg"

    if len(sys.argv) > 1:
        img = cv2.imread(img_path)
    else:
        img = np.zeros( (512, 512, 3), np.uint8 )
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle, img)

    while(1):
        
        cv2.imshow('image', img)
        
        k = cv2.waitKey(1) & 0xFF
        if (k == 27):
            break

    cv2.destroyAllWindows()
