import cv2


cap = cv2.VideoCapture(0)
img_counter = 0  

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Webcam', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
   
    if key == ord('c'):
        for i in range(30):
            ret, frame = cap.read()
            if not ret:
                break
            img_name = f"captured_image_{img_counter}.jpg"  
            cv2.imwrite(img_name, frame)
            
            img_counter += 1  
    
    
    if key == ord('q'):
        print("Exiting...")
        break


cap.release()
cv2.destroyAllWindows()
