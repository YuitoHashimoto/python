import cv2
import numpy as np

img = cv2.imread("img/honda.jpg")
# 画像サイズプリント
print(img.shape)

# 画像リサイズ
imgResize = cv2.resize(img, (500,500))
print(imgResize.shape)

# 画像トリミング
imgCropped = imgResize[0:470,0:500]

cv2.imshow("img", img)
cv2.imshow("imgResize", imgResize)
cv2.imshow("imgCropped", imgCropped)

cv2.waitKey(0)