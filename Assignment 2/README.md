# 1. Algorithm convert RGB to grayscale
* Original: Y = 0.281R + 0.562G + 0.093B
* Shifter:  Y = (R >> 2) + (R >> 5) + (G >> 1) + (G >> 4) + (B >> 4) + (B >> 4) + (B >> 5)
# 2. Convert RGB to Grayscale using python
* Using the Original algorithm to convert given in header 1
# 3. Convert RGB to Grayscale using verilog
* **Step 1:** Convert Image file (.png, .jpg, ...) to binary text file
     + Using RGB2Binary.py
     + Preprocessing with opencv python 
     + Load RGB image into text file (.txt) as binary
* **Step 2:** Convert RGB (binary file) to Grayscale as binary file using verilog module
     + Using rgb2grayscale.v and Lab1_tb.v using modelsim
     + Read binary file with ```$readmemb```
     + Save the Grayscale value after convert into text file as binary
* **Step 3:** Convert the binary file to Image and display
     + Using Binary2Grayscale.py
     + Read the binary file and save it as image grayscale
     + Display on the screen
* **Step 4:** Run all the project with one python file
     + Using main.py with os module in python
     + Type the following command to open modelsim without go inside it's path:
          - Open the terminal
          - Type: ```nano ~/.bashrc``` to open bashrc
          - At the end of this file type: ```PATH=/home/trungnguyen/intelFPGA_pro/20.4/modelsim_ase/linuxaloem:$PATH```
          - Press ```Ctrl + x``` to save this file and exit
          - Type: ```source ~/.bashrc``` and press ```Enter```
          - Restart your PC
          - Open terminal and type ```vsim```, modelsim will be opened
     + Now you can run main.py
# 4. Compare the result of two methodes
