import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.pyplot as plt

daily = pd.read_csv(r'examples_data\SP500_NOV2019_Hist.csv', index_col=0, parse_dates=True)

print(daily.head())

daily.index.name = "Date"

# 简单定义：
# 1.如果收盘价比开盘价低5，做黄色标记
# 2.如果开盘价比收盘价高5，做红色标记
red_list = []
yellow_list = []
for _, row in daily.iterrows():
    if row["Open"] - row["Close"] > 5:
        red_list.append(row["Close"])
    else:
        red_list.append(np.NaN)
    if row["Close"] - row["Open"] > 5:
        yellow_list.append(row["Open"])
    else:
        yellow_list.append(np.NaN)

# 旧版
# add_plot = [
#     mpf.make_addplot(red_list, scatter=True, markersize=200, marker='^', color='r'),
#     mpf.make_addplot(yellow_list, scatter=True, markersize=200, marker='^', color='y')
# ]

# 新版增加了样式：‘bar’, ‘ohlc’, and ‘candle’
add_plot = [
    mpf.make_addplot(red_list, type="scatter", markersize=200, marker='^', color='r'),
    mpf.make_addplot(yellow_list, type="scatter", markersize=200, marker='^', color='y')
]

mpf.plot(daily, type='candle', addplot=add_plot)

plt.show()
