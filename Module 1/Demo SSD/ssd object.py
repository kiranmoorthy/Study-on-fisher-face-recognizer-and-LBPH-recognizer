import cv2
import numpy as np

winName = 'Laptop Webcam'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

valid_classes = ['person', 'car', 'truck', 'bus', 'train', 'motorcycle', 'bicycle','cell phone']

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
   

    classIds, confs, bbox = net.detect(frame, confThreshold=0.5)
    print(classIds, bbox)

    valid_object_detected = False
    if isinstance(classIds, np.ndarray):
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            if classId - 1 < len(classNames):
                className = classNames[classId - 1]
                if className in valid_classes and confidence > 0.5:
                    valid_object_detected = True
                    x, y, w, h = box
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around the object
                    cv2.putText(frame, className, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Add object label

    cv2.imshow(winName, frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
