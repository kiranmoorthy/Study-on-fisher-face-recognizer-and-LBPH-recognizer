
import cv2
import numpy as np
 
img = cv2.imread('jack.PNG')
print(img.shape)

cv2.imshow("original", img)
 

cropped_image = img[100:400, 100:730]
 

cv2.imshow("cropped", cropped_image)
 

cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
