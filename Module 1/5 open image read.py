import cv2

image_path = r'F:\Cources\AI\Basic\image\jack.PNG'

image = cv2.imread(image_path)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
