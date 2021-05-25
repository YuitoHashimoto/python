import cv2
img = cv2.imread('chrome.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY_INV)

cv2.imshow('OpenCV', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()