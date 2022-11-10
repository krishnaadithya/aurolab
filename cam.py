import numpy as np
import cv2
import time

# The duration in seconds of the video captured
capture_duration = 10

cap = cv2.VideoCapture(2)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        out.write(frame)
         cv2.imshow('frame',frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()