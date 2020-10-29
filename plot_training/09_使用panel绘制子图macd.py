import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class DataFinanceDraw:

    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self, file: str):
        data = pd.read_csv(file)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)  # index要是Date列
        self.data = data

    def panel_draw(self):
        data = self.data
        # add_plot = [
        #     mpf.make_addplot(data, type='candle', panel=2)
        # ]
        #
        # mpf.plot(data, type="candle", mav=(2, 5), addplot=add_plot,
        #          volume=True,
        #          figscale=1.5,
        #          title='Candle',
        #          figratio=(5, 5),
        #          ylabel='price',
        #          ylabel_lower='volume')

        # 更改子图位置编号
        add_plot = [
            mpf.make_addplot(data, type='candle', panel=1)
        ]

        mpf.plot(data, type="candle", mav=(2, 5), addplot=add_plot,
                 volume=True,
                 figscale=1.5,
                 title='Candle',
                 figratio=(5, 5),
                 ylabel='price',
                 ylabel_lower='volume',
                 panel_ratios=(1, 0.3, 0.8, 0.5), num_panels=4,  # 设置子图比例
                 main_panel=0, volume_panel=2, )

    def panel_draw_macd(self):
        data = self.data

        # 计算macd
        exp12 = data["Close"].ewm(span=12, adjust=False).mean()
        exp26 = data["Close"].ewm(span=26, adjust=False).mean()
        macd = exp12 - exp26
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        # 添加macd子图
        add_plot = [
            mpf.make_addplot(exp12, type='line', color='y'),
            mpf.make_addplot(exp26, type='line', color='r'),
            mpf.make_addplot(histogram, type='bar', width=0.7, panel=2, color='dimgray', alpha=1, secondary_y=False),
            mpf.make_addplot(macd, panel=2, color='fuchsia', secondary_y=True),
            mpf.make_addplot(signal, panel=2, color='b', secondary_y=True),

        ]

        mpf.plot(data,
                 type="candle",
                 addplot=add_plot,
                 volume=True,
                 figscale=1.5,
                 title='MACD',
                 figratio=(5, 5),
                 ylabel='price',
                 ylabel_lower='volume',
                 main_panel=0,
                 volume_panel=1,
                 tight_layout=True,
                 )



dfd = DataFinanceDraw()
dfd.load_data(r'examples_data\SP500_NOV2019_Hist.csv')
# dfd.panel_draw()
dfd.panel_draw_macd()
