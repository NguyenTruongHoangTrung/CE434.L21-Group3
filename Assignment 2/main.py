import os
#Read file RGB2Binary.py
os.system('python3 "/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Binary.py"')

#Read 2 file module and test bench
os.system('vlog "/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/rgb2grayscale.v" "/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/Lab1_tb.v"')

#Compile them to create birnary of Gray scale image
os.system('vsim -c -do "run -all" Lab1_tb')

#Convert from binary to decimal and show result
os.system('python3 "/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/Binary2Grayscale.py"')
