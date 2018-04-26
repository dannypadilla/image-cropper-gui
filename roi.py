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

# if Drawing crop section, then true
drawing = False

# keep track of mouse points
coordinate = []

# reset the crop selection
def redraw(imgCopy):
    img = imgCopy.copy()
    return img
    

# Function to set cropped region
def draw(event, x, y, flags, param):
    global coordinate, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        coordinate = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        coordinate.append((x,y))
        drawing = False
        
        cv2.rectangle(img, coordinate[0], coordinate[1], (0, 255, 0), 1)

# ***************************************************************** #

if __name__ == "__main__":

    clear_screen_cmd = check_output(["clear", "."]).decode("utf8") # create clear cmd
    print(clear_screen_cmd) # all this does is clear the terminal screen for doc ( ctrl + l)

    print(__doc__) # prints doc info to screen

    try:
        fn = sys.argv[1] # cmd line arg for img_path or block_size?
    except:
        fn = "default/img/path"

    if len(sys.argv) > 1:
        img = cv2.imread(fn)
    else:
        img = np.zeros( (512, 512, 3), np.uint8)

    imgCopy = img.copy()
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw)

    while(1):
        cv2.imshow('image', img)
        key = cv2.waitKey(1) & 0xFF
        retry = False
        # Wait for 's' key to save                                                                                                                                          
        if key == ord('s'):
            cv2.imwrite('cropped_img.png', coords)
        # Wait for 'r' key to redraw crop region
        elif key == ord('r'):
            img = redraw(imgCopy)
        elif key == ord('c'):
            # Get coordinates from selected crop region
            coords = imgCopy[coordinate[0][1]:coordinate[1][1], coordinate[0][0]:coordinate[1][0]]
            # Display cropped region
            cv2.imshow("Cropped Region", coords)
        # Wait for 'q' key to exit
        elif key == ord('q'):
            break
    cv2.destroyAllWindows()
