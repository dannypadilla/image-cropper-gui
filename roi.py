'''
This program provides something.... 
* 1. Do 
* 2. Then that

Usage:
 roi.py [<some_args>, here]

Output:
 Stores an image... somewhere
'''
import cv2
import numpy as np
import os, sys
from subprocess import check_output

# Drawing crop section
drawing = False
coordinate = []

# Global Coordinates (begin at this point)
ix = -1
iy = -1


def redraw(img):
    pass


# Function to set cropped region
def draw(event, x, y, flags, param):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(img, (x, y), (ix,iy), (0, 255, 0), 1)


# ***************************************************************** #

if __name__ == "__main__":

    clear_screen_cmd = check_output(["clear", "."]).decode("utf8") # create clear cmd
    print(clear_screen_cmd) # all this does is clear the terminal screen for doc ( ctrl + l)

    print(__doc__) # prints doc info to screen

    try:
        fn = sys.argv[1] # cmd line arg for img_path or block_size?
    except:
        fn = "default/img/path"

    #print(fn) # should error check if argv is passed and valid

    img = np.zeros( (512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw)

    #img2 = img.copy

    while(1):
        cv2.imshow('image', img)
        key = cv2.waitKey(1) & 0xFF

        # Wait for 's' key to save
        if key == ord('s'):
            cv2.imwrite('image.png', img)
        # Wait for 'r' key to redraw crop region
        elif key == ord('r'):
            img
        # Wait for 'q' key to exit
        elif key == ord('q'):
            break
    cv2.destroyAllWindows()
