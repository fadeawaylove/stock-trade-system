import datetime

import matplotlib.pyplot as plt
import pandas_datareader.data as web

from strategy import linear_regression

df_stock = web.DataReader("600873.SS", "yahoo", datetime.datetime(2017, 1, 1), datetime.datetime(2020, 11, 3))
df_stock.fillna(method="bfill", inplace=True)  # 后一个数据填充NAN1

data_y, *_, degree = linear_regression(df_stock)

plt.plot(df_stock.index, data_y)
plt.plot(df_stock.index, df_stock.Close)
plt.title("600797")
plt.legend(["data", "fit_data"], loc="best")
plt.show()
