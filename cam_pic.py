import cv2
import time

def capture_photo(i):
    cap = cv2.VideoCapture(2)
    ret, frame = cap.read()
    cv2.imwrite('photo'+str(i)+'.jpg', frame)
    cap.release()

if __name__ == '__main__':
    i=0
    while True:
        capture_photo(i)
        time.sleep(4)
        i+=1