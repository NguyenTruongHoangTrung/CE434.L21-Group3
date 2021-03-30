import cv2
import time

# video = cv2.VideoCapture('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Nhu_Cute.mp4')

# width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print('Width: ', width, ', Height: ', height)

# format = 'MP4V'
# fourcc = cv2.VideoWriter_fourcc(*format)
# out = cv2.VideoWriter('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Nhu_Cute_Preprocessing.mp4', fourcc, 30, (350,640))
 
# while True:
#     ret, frame = video.read()
#     if ret == True:
#         b = cv2.resize(frame,(350,640),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
#         out.write(b)
#     else:
#         break


video = cv2.VideoCapture('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Nhu_Cute_Preprocessing.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
speed = int(1000/fps) # time for display a image
print('Fps: ', fps)
print('Time for display a image: ', speed, 'ms')

count_frame = 0

if(video.isOpened()):
	while(video.isOpened()):
		pre_time = time.time()
		# ========================= Read and pre-process video =========================
	    # read video
		check, frame = video.read()
		if(check == False):
			break

		cv2.imshow("Nhu_Cute", frame)
		cv2.imwrite('/home/viet/Documents/UIT/CE434.L21-Group3/Additional_File/Image_Preprocessing/image_'+str(count_frame)+'.jpg', frame)
		count_frame = count_frame + 1

		delta_time = (time.time() - pre_time) * 1000
		delay_time = int(speed - delta_time)
		print(delay_time)
		if delay_time > 0:
			key = cv2.waitKey(delay_time)
		else:
			key =  cv2.waitKey(1)

		if key == ord('q'): 
			break

	video.release()
	cv2.destroyAllWindows()
else:
	print('Fail to load video')

print('a number of images: ', count_frame)
