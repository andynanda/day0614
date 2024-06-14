# 尺寸转换方法
# resize()

import cv2 as cv

# 读取图片
img = cv.imread("mycat.png")
# 修改尺寸
img_resized = cv.resize(img, (200, 200))
# 显示原图
cv.imshow("cat01", img)
# 显示修改尺寸后的图
cv.imshow("cat01_resized", img_resized)
# 打印原图和修改图的尺寸
print("原图大小:", img.shape, "\n修改后大小:", img_resized.shape)

# 原图大小: (414, 500, 3)
# 修改后大小: (200, 200, 3)

# 3为彩色图片的通道数。
# 保存修改大小后的图片
cv.imwrite("resize_cat.png", img_resized)
# # 等待
# cv.waitKey(0)

# 按下英文输入法中的m键后退出程序
# ord('m') ：返回m的ascii码
# 按下m键时退出程序
while True:
    if ord("m") == cv.waitKey(0):
        break


# 释放内存
cv.destroyAllWindows()
