'''
This program provides something.... 
* 1. draw a box around a region-of-interest (ROI) to crop
* 2. roi is stored to disk (./cropped/)

Usage:
crop.py [<some_args>, here]

v - view cropped ROI (separate window)
c - close ROI window
s - save ROI
f - move forward
d - move back
q - quit

Output:
 Stores a cropped ROI to ./rois/

error check: for images too small, calc area of rectange
'''
import cv2
import numpy as np
import os, sys
from subprocess import check_output


''' GLOBAL VARIABLES ''' 
drawing = False # true if mouse is pressed
ix, iy = -1, -1
roi = None


# gets file names from a dir - includes file extension
# returns as a list
def get_file_names_from_dir(file_path):
    ls = []
    with os.scandir(file_path) as it:
        for entry in it:
            if not entry.name.startswith(".") and entry.is_file:
                ls.append(entry.name)
        return ls


# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, roi
    img_cpy = param.copy()
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        ix, iy = x, y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if drawing == True:
            #drawing = False
            #cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
            #cv2.rectangle(img_cpy, (ix, iy), (x, y), (0, 255, 0), 1)
            #drawing = False
    elif (event == cv2.EVENT_LBUTTONUP):
        drawing = False
        roi = (ix, iy, x, y)
        #cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
        #cv2.rectangle(img_cpy, (ix, iy), (x, y), (0, 255, 0), 1)


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
        img = np.zeros( (512, 512, 3), np.uint8 ) # for testing - black image

    # future labeling
    label = 1
    
    img_l, img_w, ch = img.shape
    img_cpy = img.copy()
    cv2.namedWindow("image")
    #cv2.setMouseCallback("image", draw_rectangle, img)
    cv2.setMouseCallback("image", draw_rectangle, img_cpy)

    global_roi_counter = 0
    local_roi_counter = 0
    img_counter = 1

    while(1):
        #cv2.imshow("image", img)
        cv2.imshow("image", img_cpy)
        
        k = cv2.waitKey(1) & 0xFF
        
        if (k == 27 or k == ord("q") ): # exit
            print("\n\tQ was pressed\n")
            global_roi_counter += local_roi_counter
            print(str(global_roi_counter) + " ROI(s) were stored!\n")
            break
        elif (k == ord("f") ): # move forward to next image
            print("\n\tNext Image - *not implemented yet*")
            img_counter += 1 # for file name purposes
            global_roi_counter += local_roi_counter
            local_roi_counter = 0
        elif (k == ord("d") ): # move back to prev image
            print("\n\tPrevious Image - *not implemented yet*")
            img_counter -= 1 # for file name purposes
            global_roi_counter += local_roi_counter
            local_roi_counter = 0
        
        if (roi is not None): # if ROI has been created
            x, y, w, h = roi
            
            ''' handle different mouse dragging directions '''
            if (y > h and x > w): # lower right to upper left
                img_roi = img[h:y, w:x]
            elif (y < h and x > w): # upper right to lower left
                img_roi = img[y:h, w:x]
            elif (y > h and x < w): # lower left to upper right
                img_roi = img[h:y, x:w]
            else: # upper left to bottom right
                img_roi = img[y:h, x:w]
                
            if (k == ord("v") ): # view roi
                print("\n\tViewing ROI "  + str(roi) )
                cv2.imshow("roi", img_roi)
                cv2.moveWindow("roi", img_w, 87)
            elif(k == ord("s") ): # save roi after viewing it
                path = "rois/cropped_img_" + str(img_counter) + ".jpg"
                print("\n* Saved ROI #" + str(local_roi_counter) + " " + str(roi) + " to: " + path)
                cv2.imwrite(path, img_roi)
                img_counter += 1
                cv2.destroyWindow("roi")
                roi = None
            elif(k == ord("c") ): # clear roi
                print("\n\tCleared ROI " + str(roi) )
                cv2.destroyWindow("roi")
                roi = None

    cv2.destroyAllWindows()
