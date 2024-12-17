import cv2
import numpy as np


img = cv2.imread('jack.PNG')

red_img = np.zeros_like(img)
red_img[:, :, 0] = 255


alph = 5  
blended_img = cv2.addWeighted(img, 1 - alph, red_img, alph, 0)

cv2.imshow('Blended Image', blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
