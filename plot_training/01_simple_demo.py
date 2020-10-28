import pandas as pd
import mplfinance as mpf

daily = pd.read_csv(r'examples_data\SP500_NOV2019_Hist.csv', index_col=0, parse_dates=True)

print(daily.head())

daily.index.name = "Date"


mpf.plot(daily, type='candle')

"""
新版的mplfinance的plot方法，数据对象必须是dataFram类型，并且数据列也有严格的要求。
必须包含’Open’, ‘High’, ‘Low’ 和 ‘Close’ 数据
（注意:区分大小写，这个把我也折腾了好一阵），而且行索引必须是Date，
并且是pandas.DatetimeIndex类型，行索引的名称必须是’Date‘(注意大小写)，
此外还有一列是’Volume’（成交量），这一列不是必须的，可选项（不选择绘制成交量的话，
就不会有问题）。
"""