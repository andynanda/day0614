# 图像灰度化的目的是为了简化矩阵，提高运算速度。
# 彩色图像中的每个像素颜色由R、G、B三个分量来决定，而每个分量的取值范围都在0 - 255
# 之间，这样对计算机来说，彩色图像的一个像素点就会有256 * 256 * 256 = 16777216
# 种颜色的变化范围！
# 而灰度图像是R、G、B分量相同的一种特殊彩色图像，对计算机来说，一个像素点的变化范围只有0 - 255这256种。
# 彩色图片的信息含量过大，而进行图片识别时，其实只需要使用灰度图像里的信息就足够了，所以图像灰度化的目的就是为了提高运算速度。
# 当然，有时图片进行了灰度处理后还是很大，也有可能会采用二值化图像（即像素值只能为0或1）。


# 2.2 所需方法
# 2.2.1 设置灰度方法
#     cvtColor()
#  2.2.2 保存图片方法
#     imwrite()
# 导入模块
import cv2 as cv

# 读取图片
img = cv.imread("mycat.png")

# 显示原始图片
cv.imshow("showcat", img)

# 图片灰度化
# img_gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 展示灰度化图片
cv.imshow("showcat_gray", img_gray)

# 保存灰度化图片
cv.imwrite("graycat02.png",img_gray)

# 等待
cv.waitKey(0)
# 释放资源
cv.destroyAllWindows()


# 上述代码中的 cv2.imread('image.png', cv2.IMREAD_UNCHANGED) 用于读取带有 Alpha 通道的图像。
# 如果图像没有 Alpha 通道，image_bgra.shape[2] 将返回 3，表示图像只有 BGR 三个通道。在这种情况下，
# 你不能直接使用 COLOR_BGRA2GRAY 进行转换，而应该使用 COLOR_BGR2GRAY。
# import cv2
#
# # 读取 BGRA 图像
# image_bgra = cv2.imread('mycat.png', cv2.IMREAD_UNCHANGED)  # 使用 IMREAD_UNCHANGED 保留 Alpha 通道
#
# # 检查图像是否有 Alpha 通道
# if image_bgra.shape[2] == 4:
#     # 将 BGRA 图像转换为灰度图像
#     gray_image = cv2.cvtColor(image_bgra, cv2.COLOR_BGRA2GRAY)
#
#     # 显示或保存灰度图像
#     cv2.imshow('Gray Image', gray_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("The image does not have an alpha channel.")

# 在OpenCV中，当你读取一张图片时，它会被加载为一个NumPy数组（通常称为“矩阵”或“张量”在更通用的上下文中），其中包含了图片的像素数据。
# 每个像素的颜色值（对于彩色图像）通常是以BGR（蓝色、绿色、红色）或BGRA（包括Alpha透明度通道）的顺序存储的。
# 以下是如何使用OpenCV读取图片并获取其矩阵（NumPy数组）的示例：
# import cv2
#
# # 读取图片
# image = cv2.imread('graycat02.png')  # 默认情况下，如果图片包含Alpha通道，OpenCV会忽略它
#
# # 检查图片是否成功加载
# if image is not None:
#     # 在这里，image就是一个NumPy数组（即矩阵），包含了图片的所有数据
#     # 你可以通过image.shape来获取图片的尺寸（高度、宽度和通道数）
#     height, width, channels = image.shape
#     print(f"Image size: {height}x{width} with {channels} channels")
#
#     # 你可以直接访问像素值
#     # 例如，访问第一行第一列的像素值（注意索引是从0开始的）
#     pixel_value = image[0, 0]
#     if channels == 3:  # 对于BGR图片
#         blue, green, red = pixel_value
#     elif channels == 4:  # 对于BGRA图片（如果图片包含Alpha通道并且你以cv2.IMREAD_UNCHANGED方式读取）
#         blue, green, red, alpha = pixel_value
#     print(f"Pixel value at (0, 0): {pixel_value}")
#
#     # 显示图片
#     cv2.imshow('Image', image)
#     cv2.waitKey(0)  # 等待任意按键按下
#     cv2.destroyAllWindows()  # 关闭所有OpenCV窗口
# else:
#     print("Error: Could not read the image.")
