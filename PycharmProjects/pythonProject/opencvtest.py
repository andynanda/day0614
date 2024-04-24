import cv2  # 导入opencv库

if __name__ == '__main__':
    while True:
        img_RGB = cv2.imread('/home/zme/li/imgs/16.jpg', 1)  # 获取路径img/0.jpg的图像，图像类型为RGB图像
        img_g = cv2.imread('/home/zme/li/imgs/15.jpg', 0)  # 获取路径img/0.jpg的图像，图像类型为灰度图

        '''
        # 此处为改变图像大小，在此处使用是为了演示方便，为图像预处理阶段，与获取图像无关
        img_RGB = cv2.resize(img_RGB, (0, 0), fx=0.5, fy=0.5)  # 改变图像shape
        img_g = cv2.resize(img_g, (0, 0), fx=0.5, fy=0.5)  # 改变图像shape
        '''

        cv2.imshow("RGB", img_RGB)  # 显示彩图
        cv2.imshow("gray", img_g)  # 显示灰度图
        cv2.waitKey(1)  # 等待时间


