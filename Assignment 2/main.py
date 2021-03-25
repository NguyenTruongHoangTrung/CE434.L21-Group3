import os
# Run RGB2Binary.py to convert RGB Image to Binary txt file
os.system('python3 /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Python_Script/RGB2Binary.py')

# Compile module verilog and testbench
os.system('vlog /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Verilog/rgb2grayscale.v /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Verilog/rgb2grayscale_tb.v')

# Run simulation
os.system('vsim -c -do "run -all" rgb2grayscale_tb')

# Convert Binary to Decimal and display result
os.system('python3 /home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Python_Script/Binary2Grayscale.py')
