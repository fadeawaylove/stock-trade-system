import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

daily = pd.read_csv(r'examples_data\SP500_NOV2019_Hist.csv', index_col=0, parse_dates=True)

print(daily.head())

daily.index.name = "Date"

# 添加单个数据
# add_plot = mpf.make_addplot(daily["Volume"])

# 添加多个数据
add_plot = mpf.make_addplot(daily[["Volume", "Open"]])

mpf.plot(daily, type='candle', addplot=add_plot)

plt.show()
