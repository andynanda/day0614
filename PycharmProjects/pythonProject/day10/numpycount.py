# 数值计算

import cv2

from day09 import cv_show

img_cat=cv2.imread('../imgs/cat.jpg')
img_dog=cv2.imread('../imgs/dog.jpg')

img_cat2= img_cat +10
print(img_cat[:5, :, 0])

print(img_cat2[:5, :, 0])
#
# #相当于% 256
# (img_cat + img_cat2)[:5,:,0]
#
# cv2.add(img_cat,img_cat2)[:5,:,0]