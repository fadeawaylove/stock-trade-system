import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime

import statsmodels.api as sm
from statsmodels import regression
import matplotlib.pyplot as plt

"""
Statsmodels是Python中一个强大的统计分析包，包含了回归分析、时间序列分析、假设检验等等的功能
"""
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1.获取数据
df_stockload = web.DataReader("600797.SS", "yahoo", datetime.datetime(2019, 10, 1), datetime.datetime(2020, 4, 1))
df_stockload.fillna(method="bfill", inplace=True)  # 后一个数据填充NAN1
print(df_stockload.info)

y_arr = df_stockload.Close.values
x_arr = np.arange(0, len(y_arr))
x_b_arr = sm.add_constant(x_arr)  # 添加常数

model = regression.linear_model.OLS(y_arr, x_b_arr).fit()  # 使用OLS做拟合

rad = model.params[1]  # y = kx + b : params[1] = k
intercept = model.params[0]

reg_y_fit = x_arr * rad + intercept

print(model.params)
print(np.rad2deg(rad))


# 绘图
plt.plot(x_arr, y_arr)
plt.plot(x_arr, reg_y_fit, 'r')
plt.title(f"浙大网新 y = {rad} * x + {intercept}")
plt.legend(['close', 'linear'], loc='best')

plt.show()
