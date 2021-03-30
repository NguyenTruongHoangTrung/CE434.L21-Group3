import cv2
import time
import os, os.path

format = 'MP4V'
fourcc = cv2.VideoWriter_fourcc(*format)
gray_scale_video = cv2.VideoWriter('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Gray_Nhu_Cute.mp4', fourcc, 30, (350,640))

speed = 32 # time to display a image

os.chdir('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Image_Preprocessing/')
print(os.getcwd())

num_image = len([name for name in os.listdir('.') if os.path.isfile(name)])
print('a number of images: ', num_image)

for i in range(num_image):
	pre_time = time.time()
	img = cv2.imread('image_'+str(i)+'.jpg')
	# ========================= Read and pre-process video =========================
    # read video
	gray_scale_video.write(img)

	cv2.imshow("gray scale - Nhu_cute", img)

	delta_time = (time.time() - pre_time) * 1000
	delay_time = int(speed - delta_time)
	print(delay_time)
	if delay_time > 0:
		key = cv2.waitKey(delay_time)
	else:
		key =  cv2.waitKey(1)
	if key == ord('q'): 
		break

os.chdir('..')
print(os.getcwd())
os.chdir('../python')
print(os.getcwd())

gray_scale_video.release()
cv2.destroyAllWindows()
