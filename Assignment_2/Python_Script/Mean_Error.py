import numpy as np
import cv2
import os, os.path

os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_After_Processing/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/')

error_total = 0
for i in range(num_image):
	gray_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_After_Processing/gray_scale_image_'+str(i)+'.png', cv2.IMREAD_UNCHANGED)
	rgb_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_Before_Processing/image_resized_'+str(i)+'.png', cv2.IMREAD_UNCHANGED)
	gray_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_After_Processing/gray_scale_image_0.png', cv2.IMREAD_UNCHANGED)
	rgb_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_Before_Processing/image_resized_0.png', cv2.IMREAD_UNCHANGED)

	gray_3_channels = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)      
	concate_Hor = np.concatenate((rgb_img, gray_3_channels), axis=1)   
	""" Calculate the error between the original equation and shift equation """
	# original euqation: r*0.281 + g*0.562 + b*0.093 
	# shift equation: (r >> 2) + (r >> 5) + (g >> 1) + (g >> 4) + (b >> 4) + (b >> 5)
	python_output = rgb_img[:, :, 2] * 0.281 + rgb_img[:, :, 1] * 0.562 + rgb_img[:, :, 0] * 0.093
	error = np.absolute(gray_img.astype('float32') - python_output) / python_output
	error = error.mean()
	# error_total = error + error_total
	# print(i)
	print('Error: {:.6f}%'.format(error * 100))
# print(error)

 
# error_total = error_total/num_image
# print('Error: {:.6f}%'.format(error_total * 100))