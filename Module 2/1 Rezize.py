
import cv2

img = cv2.imread('jack.PNG')
print(img.shape)

resized = cv2.resize(img, (100, 100))

cv2.imshow('Resized Image', resized)
cv2.imwrite('resized_jack.png', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



