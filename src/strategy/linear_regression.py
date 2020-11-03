"""
选股
线性回归显示股票的趋势
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels import regression


def linear_regression(data: pd.DataFrame):
    """
    https://www.statsmodels.org/
    :param data: 数据集中要包含收盘价Close
    :return: 拟合的y，k，b以及k转化的角度
    """
    y_arr = data.Close.values
    x_arr = np.arange(0, len(y_arr))
    b_arr = sm.add_constant(x_arr)
    model = regression.linear_model.OLS(y_arr, b_arr).fit()
    b, k = model.params  # y = kx + b : params[1] = k
    y_fit = x_arr * k + b
    return y_fit, k, b, np.rad2deg(k)
