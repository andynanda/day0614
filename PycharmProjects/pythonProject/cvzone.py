import cv2
import mediapipe as mp

# cvzone 手跟踪模块
cap = cv2.VideoCapture(0)
# 配置摄像头捕捉框大小
cap.set(3, 1280)
cap.set(4, 720)

while True:
    #如果读取成功，则开启摄像头
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
