import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Webcam', frame)
    
    
    if cv2.waitKey(1) == ord('c'):
        cv2.imwrite('mugesh.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
