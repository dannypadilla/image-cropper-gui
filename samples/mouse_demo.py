import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # img, center, radius, color, thickness,..
        cv2.rectangle(img, (x,y), 100, (255,0,0), 1)
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), 1)

# Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("front98.jpg", 1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
