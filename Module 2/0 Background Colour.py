import cv2

img = cv2.imread('jack.PNG')

print(img)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("orginal image",img)

#cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
