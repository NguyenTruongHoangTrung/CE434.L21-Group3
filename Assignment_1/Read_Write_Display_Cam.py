import cv2
#Open camera
cap = cv2.VideoCapture(0)

#Get the frame size
#Default is 640x480
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print('Frame size: ', (frame_width, frame_height))

#Use fourcc to specify the file format
#Example: XVID, MJPG, X264, ...
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Determine the output format (file's name, codec code, fps, frame size)
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (frame_width, frame_height))

#Use cap.isOpened () to check if the camera is valid or not 
print('Camera is valid ?  ', cap.isOpened())

while(cap.isOpened()):
    #Read cam
    _, frame = cap.read()
    
    #Flip the frame
    flip_frame = cv2.flip(frame, 1)
    
    #Write cam
    out.write(flip_frame)

    #Display cam
    cv2.imshow('frame', flip_frame)

    #Check if q is pressed then exit
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
    
#Release cam
cap.release()

#Release file
out.release()

#Close all window
cv2.destroyAllWindows()
