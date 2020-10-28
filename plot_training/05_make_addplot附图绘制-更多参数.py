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

add_plot = [
    # scatter 散点图
    mpf.make_addplot(red_list, type="scatter", markersize=200, marker='^', color='r'),
    mpf.make_addplot(yellow_list, type="scatter", markersize=200, marker='^', color='y'),
    # dashdot 点虚线
    mpf.make_addplot(daily[["High", "Low"]], linestyle='dashdot'),
    # dotted 散点图
    mpf.make_addplot(daily["Open"] - daily["Close"], linestyle="dotted", secondary_y=True),
    # 添加附图，使用panel参数
    mpf.make_addplot(daily["Volume"], panel=1, color='g', secondary_y='auto'),

]

# panel_ratios设置主图和附图的比例（两个附图panel_ratios=(1, 1，0.5)）
mpf.plot(daily, type='candle', panel_ratios=(1, 0.5), volume=True, addplot=add_plot, style='default')

plt.show()

# https://qdhhkj.blog.csdn.net/article/details/105783640