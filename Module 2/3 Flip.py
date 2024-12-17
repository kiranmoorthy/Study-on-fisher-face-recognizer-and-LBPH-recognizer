import cv2

img = cv2.imread('jack.PNG')
flipped = cv2.flip(img, 1)

cv2.imshow('Flipped Image', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
