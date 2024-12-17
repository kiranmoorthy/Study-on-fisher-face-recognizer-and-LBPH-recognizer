import cv2
import numpy as np  


x = 0
y = 0
w = 300
h = 300


image = np.zeros((400, 400, 3), dtype=np.uint8)


cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 5)   


cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
