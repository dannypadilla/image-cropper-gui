import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix, iy = -1, -1
img = None


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            #tmp = param.copy() # could also pass global img instead of param
            tmp = img.copy()
            cv2.rectangle(tmp, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', tmp)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)


img = np.zeros( (512, 512, 3), np.uint8)
tmp_img = img.copy()
first = True

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle, tmp_img)
cv2.imshow('image', img)
print(first)

while(1):
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    if(k == ord("r") ): # refresh img
        print("\nr was pressed\n")
        tmp_img = img.copy()
        #cv2.imshow('image', tmp_img)
    
cv2.destroyAllWindows()
