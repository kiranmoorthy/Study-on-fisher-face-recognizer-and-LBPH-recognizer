import cv2


path = cv2.CascadeClassifier('haarcascade_eye.xml')


video_capture = cv2.VideoCapture(0)

while True:
       
        ret, frame = video_capture.read()

        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       
        objects = path.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            
            text = "Object Detected"
        # Set the position for the text
            text_position = (x, y - 10)
        # Add the text to the frame
            cv2.putText(frame, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

       
        cv2.imshow('Video', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


video_capture.release()
cv2.destroyAllWindows()

