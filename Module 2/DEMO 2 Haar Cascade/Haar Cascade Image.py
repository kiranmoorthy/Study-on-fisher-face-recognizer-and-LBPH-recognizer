import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


image_path = 'F:\Cources\AI\Basic\image\mugesh.JPG' 
image = cv2.imread(image_path)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('Faces found', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
