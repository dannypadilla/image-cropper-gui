
''' 
modes 
     * mode is optional, if ommited 'r' will be assumed
r - read (DEFAULT)
w - writing (existing file with the same name will be erased)
x - exclusive creation, failing if the file already exists
a - append
     * any data written to the file is automatically added to the end
r+ - opens the file for both reading and writing
b - binary mode (use if no txt is used)
t - text mode (DEFAULT)

'''
import cv2
import os
import sys
#import glob


def get_file_names_from_dir(file_path):
    ls = []
    with os.scandir(file_path) as it: # python3 docs example
        for entry in it:
            if not entry.name.startswith(".") and entry.is_file:
                ls.append(entry.name) # name with file extension
        return ls

imgs_path = "./images/"
label_path = "./labels/"

label_name = "workfile"
extension = ".txt"
label = label_name + extension

f = open(label_path + label, "w")

file_names = get_file_names_from_dir(imgs_path)

for i in file_names:
    print(i, file=f)

f.close()
