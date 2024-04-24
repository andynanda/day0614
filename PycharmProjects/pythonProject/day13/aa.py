import cv2
import numpy as np

# 读取灰度图片
gray_image = cv2.imread('111.png.jpg', cv2.IMREAD_GRAYSCALE)

# 应用伪彩色映射
color_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

# 保存彩色图片
cv2.imwrite('color_image.png', color_image)

# 显示图片
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()