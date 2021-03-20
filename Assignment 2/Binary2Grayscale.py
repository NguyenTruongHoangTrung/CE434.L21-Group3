import numpy as np
import cv2

# Create empty list
arr=[]
dim=[]

# Read from file contain binary pixel and append it into arr
f = open('/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/write_mem.txt', 'r')
for x in f:
    arr.append(x)
f.close()

# print(arr)

# Remove endline
arr = list(map(lambda s: s.strip(), arr))
# print(arr)

# Read dimensions of input image after scale
f = open('Dimensions.txt', 'r')
for x in f:
    dim.append(int(x, 2))
f.close()

# get row and column of input image 
# dim = list(map(int, dim))
rows, cols = (dim[0], dim[1])
binary_lst = []
temp = 0

# Create a 2D list contain unsigned int 8 bit pixel
for i in range(rows):
    col =[]
    for j in range(cols):
        col.append(int(arr[j + temp], 2))
        if j != (cols - 1):
            continue
        else:
            temp = j + 1 + temp
    binary_lst.append(col)

print(temp)
# print(binary_lst)
print(type(binary_lst))

# Convert 2D list to 2D numpy array
binary_lst = np.array(binary_lst)
print(type(binary_lst))
# print('Convert binary to int: ', int(binary_lst, 2))

# Write the output into png file
cv2.imwrite('Grayscale_from_binary.png', binary_lst)

# Display the result
gray_img = cv2.imread('Grayscale_from_binary.png', cv2.IMREAD_UNCHANGED)
rgb_img = cv2.imread('moana_scale.png', cv2.IMREAD_UNCHANGED)
gray_3_channels = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
concate_Hor = np.concatenate((rgb_img, gray_3_channels), axis=1)
cv2.imshow('Result', concate_Hor)

# gray = r*0.281 + g*0.562 + b*0.093 
python_output = rgb_img[:, :, 2] * 0.281 + rgb_img[:, :, 1] * 0.562 + rgb_img[:, :, 0] * 0.093
error = np.absolute(gray_img.astype('float32') - python_output) / python_output
error = error.mean()
print('Error: {:.6f}%'.format(error * 100))

while (cv2.waitKey(0) & 0xff) != ord('q'):
    continue
cv2.destroyAllWindows()