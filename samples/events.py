import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]

for i in events:
    print()
    print(i)
print()

