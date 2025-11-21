import cv2

cap = cv2.VideoCapture('dog.mp4')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
        
cap.release()