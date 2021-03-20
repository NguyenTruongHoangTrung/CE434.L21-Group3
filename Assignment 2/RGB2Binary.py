import cv2
import numpy as np

# Read image file
original_img = cv2.imread('moana.jpg', cv2.IMREAD_UNCHANGED)
print('Original size: ', original_img.shape)
# cv2.imshow('Original', original_img)

# Resize original image: downscale
scale_percent = 100
height = int(original_img.shape[0] * scale_percent / 100)
width = int(original_img.shape[1]  * scale_percent / 100)
dim = (width, height)
print('Resized dimensions: ', dim)
resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)
cv2.imwrite('moana_scale.png', resized)
# print('Resized dimensions: ', resized)
# cv2.imshow('Resized', resized)
print('Resized: ', resized.shape)
convert_shape_bin = np.vectorize(np.binary_repr)
shape_bin = convert_shape_bin(np.array(resized.shape), width=13)
np.savetxt('Dimensions.txt', shape_bin, fmt='%s')

# Convert BGR to RGB
BGR2RGB_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
## cv2.imwrite('image.png', img)

# Convert 3D numpy array to 2D numpy array
img_transpose = BGR2RGB_img.transpose(2, 0, 1)
img_reshaped = img_transpose.reshape(img_transpose.shape[0], -1)

# Save integer number in file
# np.savetxt('image.txt', img_reshaped)

# Just print to check
# print(img_reshaped)

# Convert integer number to binary 8 bit width
convert_bin = np.vectorize(np.binary_repr)
img_bin = convert_bin(img_reshaped, width=8)
# https://stackoverflow.com/questions/47033153/saving-array-of-string-and-integers-to-a-text-file-in-python
np.savetxt('/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/bin.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
# print(img_bin)

# while (cv2.waitKey(0) & 0xff) != ord('q'):
#     continue
# cv2.destroyAllWindows()