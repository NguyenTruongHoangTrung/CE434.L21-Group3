import cv2
import numpy as np
import os, os.path
import glob

#Kích thước muốn resize
height = 242
width = 242
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Resized Traning Sample Cats
os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Cats/Image/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
count_frame = 0
# Resized Cat Images
for i in range(num_image):
	original_img = cv2.imread('cat.'+str(i)+'.jpg')

	dim = (width, height)
	resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)

	cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Cats/ResizedImage/cat.'+str(count_frame)+'.jpg', resized)

	""" Write dimensions into file """
	convert_shape_bin = np.vectorize(np.binary_repr)
	shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Cats/Dimensions.txt', shape_bin, fmt='%s')
	
	""" Convert BGR to RGB """
	BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	""" Convert 3D numpy array to 2D numpy array """
	img_transpose = BGR2RGB_img.transpose(2, 0, 1)
	img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

	""" Convert integer number to binary 8 bit width """
	convert_bin = np.vectorize(np.binary_repr)
	img_bin = convert_bin(img_reshaped, width=8)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Cats/Binary/number'+str(count_frame)+'.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	
	count_frame = count_frame + 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Resized Traning Sample Dogs
os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Dogs/Image/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
count_frame = 0
# Resized Cat Images
for i in range(num_image):
	original_img = cv2.imread('dog.'+str(i)+'.jpg')

	dim = (width, height)
	resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)

	cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Dogs/ResizedImage/dog.'+str(count_frame)+'.jpg', resized)

	""" Write dimensions into file """
	convert_shape_bin = np.vectorize(np.binary_repr)
	shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Dogs/Dimensions.txt', shape_bin, fmt='%s')
	
	""" Convert BGR to RGB """
	BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	""" Convert 3D numpy array to 2D numpy array """
	img_transpose = BGR2RGB_img.transpose(2, 0, 1)
	img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

	""" Convert integer number to binary 8 bit width """
	convert_bin = np.vectorize(np.binary_repr)
	img_bin = convert_bin(img_reshaped, width=8)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TrainingSample/Dogs/Binary/number'+str(count_frame)+'.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	
	count_frame = count_frame + 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Resized Test Sample Cats
os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Cats/Image/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
count_frame = 0
# Resized Cat Images
for i in range(num_image):
	original_img = cv2.imread('cat.'+str(i)+'.jpg')

	dim = (width, height)
	resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)

	cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Cats/ResizedImage/cat.'+str(count_frame)+'.jpg', resized)

	""" Write dimensions into file """
	convert_shape_bin = np.vectorize(np.binary_repr)
	shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Cats/Dimensions.txt', shape_bin, fmt='%s')
	
	""" Convert BGR to RGB """
	BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	""" Convert 3D numpy array to 2D numpy array """
	img_transpose = BGR2RGB_img.transpose(2, 0, 1)
	img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

	""" Convert integer number to binary 8 bit width """
	convert_bin = np.vectorize(np.binary_repr)
	img_bin = convert_bin(img_reshaped, width=8)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Cats/Binary/number'+str(count_frame)+'.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	
	count_frame = count_frame + 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Resized Traning Sample Dogs
os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Dogs/Image/')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
count_frame = 0
# Resized Cat Images
for i in range(num_image):
	original_img = cv2.imread('dog.'+str(i)+'.jpg')

	dim = (width, height)
	resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)

	cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Dogs/ResizedImage/dog.'+str(count_frame)+'.jpg', resized)

	""" Write dimensions into file """
	convert_shape_bin = np.vectorize(np.binary_repr)
	shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Dogs/Dimensions.txt', shape_bin, fmt='%s')
	
	""" Convert BGR to RGB """
	BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	""" Convert 3D numpy array to 2D numpy array """
	img_transpose = BGR2RGB_img.transpose(2, 0, 1)
	img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

	""" Convert integer number to binary 8 bit width """
	convert_bin = np.vectorize(np.binary_repr)
	img_bin = convert_bin(img_reshaped, width=8)
	
	np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Project/Dataset/TestSample/Dogs/Binary/number'+str(count_frame)+'.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
	
	count_frame = count_frame + 1