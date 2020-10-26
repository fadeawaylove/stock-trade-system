
import matplotlib.pyplot as plt#导入模块
import numpy as np




plt.hist(np.random.normal(loc=0.0, scale=1.0, size=1000), bins=30)#bins直方图的柱数
plt.show()