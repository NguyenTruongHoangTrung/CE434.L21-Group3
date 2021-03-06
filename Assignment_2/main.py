import os, os.path
import shutil
import cv2
import numpy as np

os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_Before_Processing')
num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Convert_Video_To_Image.py')
os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/RGB2Binary.py')
for i in range (num_image):
	shutil.copyfile('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Binary_Files_Before_Processing/bin_in_'+str(i)+'.txt', '/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt')
	os.system('vlog /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/RTL/rgb2grayscale.v /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/TestBench/rgb2grayscale_tb.v')
	
	#Run simulation
	os.system('vsim -c -do "run -all" rgb2grayscale_tb')
	shutil.copyfile('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt', '/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Binary_Files_After_Processing/bin_out_'+str(i)+'.txt')
	
	os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Binary2Grayscale.py')
	shutil.copyfile('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image_temp.png','/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_After_Processing/gray_scale_image_'+str(i)+'.png')
	
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt')
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt')
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image_temp.png')

os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Convert_Image_To_Video.py')
os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Mean_Error.py')
