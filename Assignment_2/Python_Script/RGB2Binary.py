import cv2
import numpy as np

""" Read image file """
#Modify path in here
#original_img = cv2.imread('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Input_Image/moana.jpg', cv2.IMREAD_UNCHANGED)
original_img = cv2.imread('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Input_Image/moana.jpg', cv2.IMREAD_UNCHANGED)

print('Original size: ', original_img.shape)
# cv2.imshow('Original', original_img)

""" Resize original image: downscale """
scale_percent = 100
height = int(original_img.shape[0] * scale_percent / 100)
width = int(original_img.shape[1]  * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(original_img, dim, interpolation=cv2.INTER_AREA)
#Modify path in here
#cv2.imwrite('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/moana_resize.png', resized)
cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/moana_resize.png', resized)

print('Resized image: ', resized.shape)

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
# print(img_reshaped) # Print the shape after convert to check

""" Convert integer number to binary 8 bit width """
convert_bin = np.vectorize(np.binary_repr)
img_bin = convert_bin(img_reshaped, width=8)
#Modify path in here
#np.savetxt('/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
np.savetxt('/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in.txt', img_bin, delimiter=' ', newline='\n', fmt='%s')
# print(img_bin)

# while (cv2.waitKey(0) & 0xff) != ord('q'):
#     continue
# cv2.destroyAllWindows()