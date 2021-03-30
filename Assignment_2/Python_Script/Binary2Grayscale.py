import numpy as np
import cv2

""" Create empty list """
arr=[]      # Store binary file as grayscale values
dim=[]      # Store dimensions of input image

""" Read and Store into arr"""
#Modify path in here
#f = open('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt', 'r')
f = open('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt', 'r')

for x in f:
    arr.append(x)
f.close()

arr = list(map(lambda s: s.strip(), arr)) # Remove endline

""" Read dimensions of input image after scale """
#Modify path in here
#f = open('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt', 'r')
f = open('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt', 'r')

for x in f:
    dim.append(int(x, 2))
f.close()

""" Get row and column of input image """
rows, cols = (dim[0], dim[1])

binary_lst=[]   # Create empty list to store the grayscale 2D matrix 
temp = 0        # Store base address
""" Create a 2D list contain unsigned int 8 bit pixel """
for i in range(rows):
    col =[]
    for j in range(cols):
        col.append(int(arr[j + temp], 2))   # Store and Convert binary to int
        if j != (cols - 1):
            continue
        else:
            temp = j + 1 + temp
    binary_lst.append(col)

""" Convert 2D list to 2D numpy array """
binary_lst = np.array(binary_lst)
print(type(binary_lst))

""" Write the output into jpg file """
#Modify path in here
#cv2.imwrite('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Grayscale_image.png', binary_lst)
cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image_temp.png', binary_lst)