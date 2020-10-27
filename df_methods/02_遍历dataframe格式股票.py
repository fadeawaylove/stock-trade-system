import datetime
import pandas_datareader.data as web

df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2018, 2, 1))

df_stockload["Ma20"] = df_stockload.Close.rolling(windows=20).mean()  # 增加M20移动平均线
print(df_stockload.head(10))











