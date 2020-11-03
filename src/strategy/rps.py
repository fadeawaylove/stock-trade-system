"""
选股
通过该指标可以反映出个股的走势在同期市场中的相对强弱表现,通过RPS指标可以初步筛选出市场中的强势股，对于选股过程来说意义重大
公式：今日收盘价/昨日收盘价-1 或者使用 DataFrame.pct_change()
来源：欧奈尔法则canslim
"""
import pandas as pd
import matplotlib.pyplot as plt


def show_rps(data: pd.DataFrame, interval: int = 1, start_index=None, show=False):
    rsp_data = data.pct_change(interval)

    if start_index:
        rsp_data = rsp_data.loc[rsp_data.index >= pd.to_datetime(start_index)]

    if show:
        plt.plot(rsp_data)
        plt.legend(data.columns, loc="best")
        plt.show()

    return rsp_data
