import cv2
import numpy as np

# 1,加载视频文件
cap = cv2.VideoCapture("los_angeles.mp4")

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
while True:
    ret, frame = cap.read()

    if (ret == True):
        # 1.灰度
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 2.去噪 （高斯）
        blur = cv2.GaussianBlur(frame, (3, 3), 0)
        # 3. 去背影
        mask = bgsubmog.apply(blur)

        # 4.腐蚀  去掉图中小斑块
        erode = cv2.erode(mask, kernel)

        # 5. 膨胀  还原放大
        dilate = cv2.dilate(erode, kernel, iterations=6)

        # 闭操作 去掉物体内部小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

        # 获取所有的轮廓
        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for (i, c) in enumerate(cnts):
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("mask", frame)
        # cv2.imshow("close", close)
        # cv2.imshow("1", dilate)
        # res = np.vstack((mask, erode, dilate,close))
        # 上下堆叠第一组图像
        # top_stack = np.vstack((mask, erode))
        # 上下堆叠第二组图像
        # bottom_stack = np.vstack((dilate, close))

        # 现在 top_stack 和 bottom_stack 各自包含两个图像，它们分别垂直堆叠在一起

        # 使用 np.hstack 将两个堆叠后的图像在水平方向上组合
        # res = np.hstack((top_stack, bottom_stack))
        # res = cv2.resize(res,(0,0),fx=0.5,fy=0.5)
        # cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if (key == 27):
        break

cap.release()
cv2.destroyAllWindows()
