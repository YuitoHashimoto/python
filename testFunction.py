import cv2
import numpy as np

img = cv2.imread("img/honda.jpg")
#カーネル定義
kernel = np.ones((5,5), np.uint8)

# 画像をぐれーにする
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 画像にぼかしをかける
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# 画像のエッジを検出
imgCanny = cv2.Canny(imgGray, 100, 100)
# エッジを拡張
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# エッジを縮小a
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("GrayImg", imgGray)
cv2.imshow("BlurImg", imgBlur)
cv2.imshow("CannyImg", imgCanny)
cv2.imshow("DialationImg", imgDialation)
cv2.imshow("ErodedImg", imgEroded)
cv2.waitKey(0)