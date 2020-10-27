import pandas_datareader.data as web
import datetime
#获取上证指数的2017.1.1日至今的交易数据
df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2017,1,1), datetime.date.today())

print(df_stockload.head())  # 查看前几行
"""
              High     Low    Open   Close  Volume  Adj Close
Date                                                         
2017-01-03  3136.5  3105.3  3105.3  3135.9  141600     3135.9
2017-01-04  3160.1  3130.1  3133.8  3158.8  167900     3158.8
2017-01-05  3168.5  3154.3  3157.9  3165.4  174700     3165.4
2017-01-06  3172.0  3153.0  3163.8  3154.3  183700     3154.3
2017-01-09  3173.1  3147.7  3148.5  3171.2  171700     3171.2
"""
print(df_stockload.tail())  # 查看末尾几行
"""
              High     Low    Open   Close  Volume  Adj Close
Date                                                         
2019-03-04  3090.8  3006.9  3015.9  3027.6  525600     3027.6
2019-03-05  3055.0  3009.4  3019.9  3054.2  424100     3054.2
2019-03-06  3103.8  3050.1  3060.4  3102.1  555000     3102.1
2019-03-07  3129.9  3075.0  3103.7  3106.4  583800     3106.4
2019-03-08  3075.0  2969.6  3038.3  2969.9  577900     2969.9
"""

print (df_stockload.columns)#查看列索引信息
"""
Index(['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'], dtype='object')
"""
print (df_stockload.index)#查看行索引信息
"""
DatetimeIndex(['2017-01-03', '2017-01-04', '2017-01-05', '2017-01-06',
               '2017-01-09', '2017-01-10', '2017-01-11', '2017-01-12',
               '2017-01-13', '2017-01-16',
               ...
               '2019-02-25', '2019-02-26', '2019-02-27', '2019-02-28',
               '2019-03-01', '2019-03-04', '2019-03-05', '2019-03-06',
               '2019-03-07', '2019-03-08'],
              dtype='datetime64[ns]', name='Date', length=530, freq=None)
"""
print(df_stockload.shape)#查看形状
"""
(530, 6)
"""

print (df_stockload.describe())#查看各列数据描述性统计

print(df_stockload.info())#查看缺失及每列数据类型

import matplotlib.pyplot as plt

#绘制收盘价
df_stockload.Close.plot(c='b')
plt.legend(['Close','30ave','60ave'],loc='best')
plt.show()