from tensorflow import keras
from keras.utils import plot_model
import numpy as np

x_train = np.random.rand(10000, 2)
y_train = 3 * x_train[:, 0] + 2 * x_train[:, 1] + 1
print(y_train.shape)

model = keras.models.Sequential()
# 使用add方法添加隐层
model.add(keras.layers.Dense(512, activation='sigmoid', input_dim=2, use_bias=True))

model.add(keras.layers.Dense(1, activation='sigmoid', use_bias=True))
# 编译模型
model.compile(loss=keras.losses.mean_squared_error,
              optimizer=keras.optimizers.Adam(0.01),
              metrics=['accuracy'])
# 训练模型
model.fit(x_train, y_train, batch_size=10)
# 输出：
10 / 1000[..............................] - ETA: 26
s - loss: 17.7002 - acc: 0.0000e+00
690 / 1000[ == == == == == == == == == = > ..........] - ETA: 0
s - loss: 12.8620 - acc: 0.0000e+00
1000 / 1000[ == == == == == == == == == == == == == == ==] - 0
s
336u
s / step - loss: 11.8523 - acc: 0.0000e+00