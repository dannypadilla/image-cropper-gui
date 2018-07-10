'''
This program provides something.... 
* 1. draw a box around a region-of-interest (ROI) to crop
* 2. roi is stored to disk (./cropped/)
* 3. x, y, w, h coordinates of ROI are stored in a txt file (./labels/)

Usage:
crop.py [<some_args>, here]

v - view cropped ROI (separate window)
c - close ROI window
r - refresh image (partial implementation)
s - save ROI
f - move forward
d - move back
q - quit

Output:
 Stores a cropped ROI to ./rois/
 Stores coords of cropped ROI as a .txt file corresponding to the img name to ./labels/

error check: for images too small, calc area of rectange
'''
import cv2
import numpy as np
import os, sys
from subprocess import check_output

''' CONSTANTS '''
LABEL = 2

''' GLOBAL VARIABLES ''' 
drawing = False # true if mouse is pressed
ix, iy = -1, -1
roi = None
img = None


# handle different mouse dragging directions
def get_roi(img, x, y, w, h):
    if (y > h and x > w): # lower right to upper left
        img_roi = img[h:y, w:x]
    elif (y < h and x > w): # upper right to lower left
        img_roi = img[y:h, w:x]
    elif (y > h and x < w): # lower left to upper right
        img_roi = img[h:y, x:w]
    elif (y == h and x == w):
        img_roi = None
    else: # upper left to bottom right
        img_roi = img[y:h, x:w]
    return img_roi


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
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        ix, iy = x, y
        
    elif (event == cv2.EVENT_MOUSEMOVE):
        if drawing == True:
            #tmp_img = param.copy()
            tmp_img = img.copy()
            cv2.rectangle(tmp_img, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.imshow("image", tmp_img)
            
    elif (event == cv2.EVENT_LBUTTONUP):
        #tmp_img = param.copy()
        tmp_img = img.copy()
        drawing = False
        roi = (ix, iy, x, y)
        cv2.rectangle(tmp_img, (ix, iy), (x, y), (0, 255, 0), 1)


if __name__ == "__main__":

    clear_screen_cmd = check_output(["clear", "."]).decode("utf8")
    print(clear_screen_cmd) # clears terminal (ctrl + l)

    print(__doc__)

    try:
        img_path = sys.argv[1]
    except:
        img_path = "../images/front10.jpg"

    # counters
    global_roi_counter = 0
    local_roi_counter = 0
    img_counter = 0

    # dir stuff
    labels_dir_path = "./labels/" # where to store label txt files
    imgs_dir_path = "./images/" # where to grab images from
    rois_dir_path = "./rois/" # where to store roi
    
    file_names_with_ext = get_file_names_from_dir(imgs_dir_path)
    file_names = [x.split(".")[0] for x in file_names_with_ext] # gets name only - discards extension
    number_of_imgs = len(file_names)

    # image stuff
    img = cv2.imread(imgs_dir_path + file_names[img_counter] + ".jpg" )
    img_l, img_w, ch = img.shape
    tmp_img = img.copy()

    # window/screen stuff
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", draw_rectangle)
    cv2.imshow("image", img)

    # i/o setup
    if (img_counter < len(file_names) ): # make sure don't go out of bound
        try:
            f = open(labels_dir_path + file_names[img_counter] + ".txt", "a+") # maybe put this is while loop
            # since it currently makes a txt file for all imgs.. even if no ROI is created
        except:
            print("File I/O error")
            exit()
    else:
        print("Reached END OF IMAGES")

    while(1):
        
        k = cv2.waitKey(1) & 0xFF
        
        if (k == 27 or k == ord("q") ): # exit
            print("\n\tQ was pressed - Quitting\n")
            global_roi_counter += local_roi_counter
            print(str(global_roi_counter) + " ROI(s) were stored!\n")
            break
        
        elif (k == ord("f") and (img_counter < number_of_imgs) ): # move forward to next image
            print("\n\tNext Image")
            roi = None
            cv2.destroyWindow("roi")
            img_counter += 1 # for file name purposes
            global_roi_counter += local_roi_counter
            local_roi_counter = 0
            f.close()
            f = open(labels_dir_path + file_names[img_counter] + ".txt", "a+")
            img_path = "./images/" + file_names[img_counter] + ".jpg"
            img = cv2.imread(img_path)
            tmp_img = img.copy()
            cv2.imshow("image", tmp_img)
            
        elif (k == ord("d") and (img_counter >= 0) ): # move back to prev image
            print("\n\tPrevious Image")
            roi = None
            cv2.destroyWindow("roi")
            img_counter -= 1 # for file name purposes
            global_roi_counter += local_roi_counter
            local_roi_counter = 0
            f.close()
            f = open(labels_dir_path + file_names[img_counter] + ".txt", "a+")
            img_path = "./images/" + file_names[img_counter] + ".jpg"
            img = cv2.imread(img_path)
            tmp_img = img.copy()
            cv2.imshow("image", tmp_img)

        elif (k == ord("r") ): # refresh image (remove all markings on img)
            print("\n\tR was pressed - REFRESH * not implemented yet")
            tmp_img = img.copy()
            cv2.imshow("image", tmp_img)
        
        if (roi is not None): # if ROI has been created
            x, y, w, h = roi
            img_roi = get_roi(img, x, y, w, h)
            
            if img_roi is None: # bug check
                print("\nERROR:\tROI " + str(roi) + " is Out-of-Bounds OR not large enough")
                cv2.destroyWindow("roi")
                roi = None
                
            elif (k == ord("v") ): # view roi
                print("\n\tViewing ROI "  + str(roi) )
                cv2.imshow("roi", img_roi)
                cv2.moveWindow("roi", img_w, 87)
                
            elif(k == ord("s") ): # save roi after viewing it
                local_roi_counter += 1
                path = rois_dir_path + file_names[img_counter] + "_" + str(local_roi_counter) + ".jpg"
                print("\n* Saved ROI #" + str(local_roi_counter) + " " + str(roi) + " to: " + path)
                cv2.imwrite(path, img_roi)
                print(str(LABEL), x, y, w, h, file=f)
                cv2.destroyWindow("roi")
                roi = None
                
            elif(k == ord("c") ): # clear roi
                print("\n\tCleared ROI " + str(roi) )
                roi = None
                cv2.destroyWindow("roi")
                tmp_img = img.copy()
                cv2.imshow("image", tmp_img)

    f.close()
    cv2.destroyAllWindows()
