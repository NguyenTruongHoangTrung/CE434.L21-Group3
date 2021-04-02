import cv2
import numpy as np
import time
import os, os.path
import glob

os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Resource/Image/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
count_frame = 0

for i in range(num_image):
	pre_time = time.time()
	original_img = cv2.imread('image_'+str(i)+'.jpg')

	scale_percent = 100
	height = int(original_img.shape[0] * scale_percent / 100)
	width = int(original_img.shape[1]  * scale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)
    #Modify path in here
    #cv2.imwrite('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/moana_resize.png', resized)
	cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_Before_Processing/image_resized_'+str(count_frame)+'.png', resized)
	print('Processing in image :', i)

	""" Write dimensions into file """
	convert_shape_bin = np.vectorize(np.binary_repr)
	shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
	
    #Modify path in here
    #np.savetxt('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt', shape_bin, fmt='%s')
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt', shape_bin, fmt='%s')
	
	""" Convert BGR to RGB """
	BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	""" Convert 3D numpy array to 2D numpy array """
	img_transpose = BGR2RGB_img.transpose(2, 0, 1)
	img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

	""" Convert integer number to binary 8 bit width """
	convert_bin = np.vectorize(np.binary_repr)
	img_bin = convert_bin(img_reshaped, width=8)
	
	#Modify path in here
	#np.savetxt('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Binary_Files_Before_Processing/bin_in_'+str(count_frame)+'.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	
	count_frame = count_frame + 1
    