import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.pyplot as plt

print(mpf.available_styles())

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
# mpf.plot(daily, type='candle', panel_ratios=(1, 0.5), volume=True, addplot=add_plot, style='default')
mpf.plot(daily, type='candle', addplot=add_plot, volume=True,
         figscale=1.5, style="blueskies",
         title=u'SP500行情', figratio=(3, 2), ylabel='price', ylabel_lower='volume',
         # savefig='my_image.png'
         )
"""
plot绘图的部分参数
:type设置图像类型'ohlc'/'candle'/'line/renko'
:mav 绘制平局线
:show_nontrading= True 显示非交易日（k线之间有间隔）,False 不显示交易日，k线之间没有间隔
:title:设置标题
:ylabel=设置主图Y轴标题
：ylabel_lower 设置成交量一栏Y坐标标题
:figratio:设置图形纵横比
:figscale 设置图像的缩小或放大,1.5就是放大50%，最大不会超过电脑屏幕大小
：style 设置整个图表样式，可以使用前面设置的样式my_style,只能在plot函数中使用指定整个图表样式，不能在make_addplot中使用。
savefig:导出图片，填写文件名及后缀,如果使用了，就不会显示图像了
"""

plt.show()

# https://qdhhkj.blog.csdn.net/article/details/105783640
