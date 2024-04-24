# 图像基本操作
#Anaconda:https://www.anaconda.com/download/
#Python_whl:https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv


"""

数据读取-图像
cv2.IMREAD_COLOR：彩色图像
cv2.IMREAD_GRAYSCALE：灰度图像
"""
import cv2 #opencv读取的格式是BGR
import inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

img1=cv2.imread('../imgs/cat.jpg')
# print(img1)

# cv2.imshow("images1",img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def cv_show(name,img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# print(img1.shape)

img2=cv2.imread('../imgs/cat.jpg',cv2.IMREAD_GRAYSCALE)
# print(img2)

#图像的显示,也可以创建多个窗口
# cv2.imshow('image1',img1)
# cv2.imshow('image2',img2)
# # 等待时间，毫秒级，0表示任意键终止
# cv2.waitKey(10000)
# cv2.destroyAllWindows()

# #保存
# cv2.imwrite('imgs/mycat.png',img1)
# cv2.imwrite('imgs/mycatgray.png',img2)

# print(type(img1))
# print(type(img2))
#
# print(img1.size)
# print(img2.size)
#
# print(img1.dtype)
# print(img2.dtype)