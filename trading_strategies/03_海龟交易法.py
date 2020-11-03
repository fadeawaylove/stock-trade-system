import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
N1 = 15
N2 = 5

df_stockload = web.DataReader("600410.SS", "yahoo", datetime.datetime(2017, 10, 1), datetime.datetime(2019, 4, 1))

df_stockload['N1_High'] = df_stockload.High.rolling(window=N1).max()  # 计算最近N1个交易日最高价

expan_max = df_stockload.Close.expanding().max()
df_stockload['N1_High'].fillna(value=expan_max, inplace=True)  # 目前出现过的最大值填充前N1个nan
print(df_stockload.head())

df_stockload['N2_Low'] = df_stockload.Low.rolling(window=N2).min()  # 计算最近N2个交易日最低价
expan_min = df_stockload.Close.expanding().min()
df_stockload['N2_Low'].fillna(value=expan_min, inplace=True)  # 目前出现过的最小值填充前N2个nan
print(df_stockload.head())

buy_index = df_stockload[df_stockload.Close > df_stockload.N1_High.shift(1)].index
print(buy_index)

sell_index = df_stockload[df_stockload.Close < df_stockload.N2_Low.shift(1)].index
print(sell_index)

df_stockload.loc[buy_index, 'signal'] = 1
df_stockload.loc[sell_index, 'signal'] = 0
print(df_stockload.head(15))

df_stockload['signal'].fillna(method='ffill', inplace=True)
print(df_stockload.signal)

# 由于收盘价格是在收盘后才确定，那么第二天才能执行给出的买卖操作，此处将signal序列使用shift(1)方法右移更接近真实情况
df_stockload['signal'] = df_stockload.signal.shift(1)

df_stockload['signal'].fillna(value=0, inplace=True)
print(df_stockload.signal)

# N日突破买卖信号区间显示
skip_days = 0

for kl_index, today in df_stockload.iterrows():
    if today.signal == 1 and skip_days == 0:  # 买入
        skip_days = -1
        start = df_stockload.index.get_loc(kl_index)
        plt.annotate('买入', xy=(kl_index, df_stockload.Close.asof(kl_index)),
                     xytext=(kl_index, df_stockload.Close.asof(kl_index) + 2),
                     arrowprops=dict(facecolor='r', shrink=0.1), horizontalalignment='left', verticalalignment='top')
        print("buy:", kl_index)
    elif today.signal == 0 and skip_days == -1:  # 卖出
        skip_days = 0
        end = df_stockload.index.get_loc(kl_index)
        if df_stockload.Close[end] < df_stockload.Close[start]:  # 赔钱显示绿色
            plt.fill_between(df_stockload.index[start:end], 0, df_stockload.Close[start:end], color='green', alpha=0.38)
        else:  # 赚钱显示红色
            plt.fill_between(df_stockload.index[start:end], 0, df_stockload.Close[start:end], color='red', alpha=0.38)
        plt.annotate('卖出', xy=(kl_index, df_stockload.Close.asof(kl_index)),
                     xytext=(kl_index + datetime.timedelta(days=5), df_stockload.Close.asof(kl_index) + 2),
                     arrowprops=dict(facecolor='g', shrink=0.1), horizontalalignment='left', verticalalignment='top')
        print("sell:", kl_index)

plt.plot(df_stockload.index, df_stockload.Close)
plt.legend(['Close'],loc='best')
plt.title(u"华胜天成 N日突破择时")
plt.show()
