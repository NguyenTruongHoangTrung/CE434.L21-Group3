import numpy as np
import cv2

""" Create empty list """
arr=[]      # Store binary file as grayscale values
dim=[]      # Store dimensions of input image

""" Read and Store into arr"""
#Modify path in here
#f = open('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt', 'r')
f = open('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out.txt', 'r')

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
cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image.png', binary_lst)

""" Concate the original image and Grayscale image """
#Modify path in here
#gray_img = cv2.imread('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Grayscale_image.png', cv2.IMREAD_UNCHANGED)
gray_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image.png', cv2.IMREAD_UNCHANGED)
#Modify path in here
#rgb_img = cv2.imread('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/moana_resize.png', cv2.IMREAD_UNCHANGED)
rgb_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/moana_resize.png', cv2.IMREAD_UNCHANGED)
gray_3_channels = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)        # rgb_img have 3 channels so we convert gray_img to 3 channels
concate_Hor = np.concatenate((rgb_img, gray_3_channels), axis=1)    # concate

""" Write and Display """
#Modify path in here
#cv2.imwrite('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Result_image.png', concate_Hor)
cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Result_image.png', concate_Hor)

cv2.imshow('Result', concate_Hor)

""" Calculate the error between the original equation and shift equation """
# original euqation: r*0.281 + g*0.562 + b*0.093 
# shift equation: (r >> 2) + (r >> 5) + (g >> 1) + (g >> 4) + (b >> 4) + (b >> 5)
python_output = rgb_img[:, :, 2] * 0.281 + rgb_img[:, :, 1] * 0.562 + rgb_img[:, :, 0] * 0.093
error = np.absolute(gray_img.astype('float32') - python_output) / python_output
error = error.mean()
print('Error: {:.6f}%'.format(error * 100))

while (cv2.waitKey(0) & 0xff) != ord('q'):
    continue
cv2.destroyAllWindows()