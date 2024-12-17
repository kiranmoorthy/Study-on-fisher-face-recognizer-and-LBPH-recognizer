import cv2
cap = cv2.VideoCapture(0)

while True:
    a, frame = cap.read()
    if not a:
        break
    cv2.imshow('Mugesh', frame)
    cv2.waitKey(3) 
           

cap.release()
cv2.destroyAllWindows()
