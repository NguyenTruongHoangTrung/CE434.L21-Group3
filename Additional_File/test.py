import glob
import cv2
import numpy as np
import time
import os, os.path

os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Bin_In/')
print(os.getcwd())

num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
print('a number of images: ', num_image)

read_files = glob.glob("*.txt")
with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())