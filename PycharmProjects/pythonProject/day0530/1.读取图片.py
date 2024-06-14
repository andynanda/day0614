# imshow和WaitKey方法
# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread("mycat.png")

# 显示图片
cv.imshow("showcat", img)

# 等待delay
# waitKey()–是在一个给定的时间内(单位ms)
# 等待用户按键触发;
# waitKey()
# 函数的功能是不断刷新图像, 频率时间为delay, 单位为ms
# 返回值为当前键盘按键值 如果用户没有按下键, 则继续等待(循环)
# 常见: 设置waitKey(0), 则表示程序会无限制的等待用户的按键事件；一般在imgshow的时候,
# 如果设置waitKey(0), 代表按任意键继续
#
# waitkey控制着imshow的持续时间，当imshow之后不跟waitkey时，相当于没有给imshow提供时间展示图像
# 所以只有一个空窗口一闪而过。添加了waitkey后，哪怕仅仅是cv2.waitkey(1),
# 我们也能截取到一帧的图像。所以cv2.imshow后边是必须要跟cv2.waitkey的。

cv.waitKey(0)

# 释放内存
cv.destroyAllWindows()
