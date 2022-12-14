import cv2
import time

cap = cv2.VideoCapture(2)

i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if i % 4 == 0:
        cv2.imwrite('photo'+str(i)+'.jpg',frame)
    i += 1
    if i == 40:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()