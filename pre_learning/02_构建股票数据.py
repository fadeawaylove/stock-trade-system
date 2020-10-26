import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dd = pd.date_range("2010-01-01", freq="D", periods=1000)


stock_data = np.random.normal(loc=10, scale=1.0, size=1000)
pct_change = np.random.normal(loc=0.0,scale=1.0, size=1000)

df_stock = pd.DataFrame({"close": stock_data, "price range": pct_change}, index=dd)

print(df_stock)


"""
区别：
series，只是一个一维数据结构，它由index和value组成。
dataframe，是一个二维结构，除了拥有index和value之外，还拥有column。
联系：
dataframe由多个列series组成，每一行还是dataframe。
"""