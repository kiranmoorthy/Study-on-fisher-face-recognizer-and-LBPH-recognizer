import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Webcam', frame)
    
    
    key = cv2.waitKey(1) 
    
  
    if key == ord('c'):
        cv2.imwrite('captured_image.jpg', frame)
       
       
    
   
    if key == ord('q'):
        print("Exiting...")
        break


cap.release()
cv2.destroyAllWindows()
