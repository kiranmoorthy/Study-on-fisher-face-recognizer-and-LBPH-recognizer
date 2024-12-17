import cv2


cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    
    cv2.imshow('Webcam', frame)
    
   
    if cv2.waitKey(1) & 0xFF == ord('c'):
        
        cv2.imwrite('F:\\Cources\\AI\\Basic\\image\\Mugeshwaran.jpg', frame)
        break


cap.release()
cv2.destroyAllWindows()