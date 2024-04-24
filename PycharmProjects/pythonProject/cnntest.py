import tensorflow as tf

input_shape = (None, 28, 28, 3)  # 输入张量的形状，(批大小，高度，宽度，通道数)
model = tf.keras.models.Sequential()  # 创建一个序列模型
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu', input_shape=input_shape[1:]))

import tensorflow as tf
import matplotlib.pyplot as plt

# 读取图片
path = r'C:\Users\yh\Pictures\rm.png'  # 替换为实际图片的路径
image_raw = tf.io.read_file(path)
image = tf.image.decode_image(image_raw, channels=3)  # 指定通道数为3

# 扩展图片维度以适应Conv2D的输入形状
input_image = tf.expand_dims(image, axis=0)

# 定义卷积层
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(filters=1, kernel_size=3, strides=1, padding='same', activation='relu',
                                 input_shape=input_image.shape[1:]))

# 运行卷积操作
convolved_image = model.predict(input_image)

# 将三个通道的卷积结果叠加
convolved_image = tf.reduce_sum(convolved_image, axis=-1)

# 转换卷积结果的形状和像素值范围
convolved_image = tf.squeeze(convolved_image, axis=0)  # 去除批处理维度
convolved_image = tf.clip_by_value(convolved_image, 0, 255)  # 将像素值裁剪到0-255范围内
convolved_image = tf.cast(convolved_image, dtype=tf.uint8)  # 转换为整数类型

# 显示原始图片和卷积结果
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(convolved_image, cmap='gray')  # 以灰度图显示卷积结果
plt.title('Convolved Image')

plt.show()