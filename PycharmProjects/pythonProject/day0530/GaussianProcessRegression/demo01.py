# 以下是一个使用高斯过程回归（Gaussian Process Regression, GPR）的简单代码案例，
# 这里我们使用Python的scikit-learn库中的GaussianProcessRegressor类来实现。

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from matplotlib import pyplot as plt

# 生成一些模拟数据
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.sin(5 * X).ravel() * 0.2 + np.random.normal(0, 0.1, X.shape[0])

# 创建一个高斯过程回归模型
# 我们使用点积核（DotProduct）和噪声核（WhiteKernel）的组合作为核函数
kernel = DotProduct() + WhiteKernel()
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0).fit(X, y)

# 绘制原始数据和预测结果
X_plot = np.linspace(0, 5, 100)[:, None]
y_pred, sigma = gpr.predict(X_plot, return_std=True)

# 绘制置信区间
plt.figure()
plt.plot(X, y, 'r.', markersize=10, label='Observations')
plt.plot(X_plot, y_pred, 'b-', label='Prediction')

# 绘制两个标准差的置信区间
plt.fill_between(X_plot[:, 0], y_pred - 2 * sigma, y_pred + 2 * sigma,
                 alpha=0.2, fc='b', ec='None', label='95% confidence interval')

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.ylim(-3, 4)
plt.legend(loc='upper left')
plt.show()