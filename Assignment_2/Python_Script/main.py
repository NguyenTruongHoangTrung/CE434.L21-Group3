import os
import shutil

os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Convert_Image_To_Video.py')
# Run RGB2Binary.py to convert RGB Image to Binary txt file
#Modi fy path in here
# os.system('python3 /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Python_Script/RGB2Binary.py')
#os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/RGB2Binary.py')

# Compile module verilog and testbench
#Modify path in here
#os.system('vlog /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Verilog/rgb2grayscale.v /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Verilog/rgb2grayscale_tb.v')
for i in range (83):
	shutil.copy2('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Binary_Files_Before_Processing/bin_in_'+str(i)+'.txt', '/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt')
	os.system('vlog /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Verilog/rgb2grayscale.v /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Verilog/rgb2grayscale_tb.v ')
	#Run simulation
	os.system('vsim -c -do "run -all" rgb2grayscale_tb')
	shutil.copyfile('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt', '/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Binary_Files_After_Processing/bin_out_'+str(i)+'.txt')
	os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Binary2Grayscale.py')
	shutil.copyfile('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image_temp.png','/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Image_After_Processing/gray_scale_image_'+str(i)+'.png')
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt')
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt')
	os.remove('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Grayscale_image_temp.png')
os.system('python3 /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Python_Script/Convert_Image_To_Video.py')
# Convert Binary to Decimal and display result
#Modify path in here
#os.system('python3 /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Python_Script/Binary2Grayscale.py')

