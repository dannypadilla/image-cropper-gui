import cv2
import numpy as np

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

img = np.zeros( (512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

#img2 = img.copy

while(1):
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF

    # Wait for ESC Key to exit
    if key == 27:
        break
cv2.destroyAllWindows()
