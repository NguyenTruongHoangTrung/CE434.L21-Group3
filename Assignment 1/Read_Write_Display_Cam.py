import cv2
#Open camera
cap = cv2.VideoCapture(0)

#Use fourcc to specify the file format 
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Determine the output format 
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (640,480))

#Use cap.isOpened () to check if the camera is valid or not 
print(cap.isOpened())

while(cap.isOpened()):
    #Read cam
    ret, frame = cap.read()

    #Write cam
    out.write(frame)

    #Display cam
    cv2.imshow('frame', frame)

    #Check if q is pressed then exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#Release cam
cap.release()

#Release file
out.release()

#Close all window
cv2.destroyAllWindows()
