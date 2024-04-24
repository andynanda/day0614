import cv2
import numpy as np

# 读取图像
img = cv2.imread('imgs/fishbot_map.pgm', 0)

# 应用中值滤波器去除噪点
denoised_img = cv2.medianBlur(img, 5)

# 显示原图和去噪后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Denoised Image', denoised_img)

# 等待按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()