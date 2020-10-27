import datetime
import tushare as ts
import pandas as pd

df_sh=ts.get_hist_data('sh',start='2017-01-01',end=datetime.datetime.now().strftime('%Y-%m-%d'))
print(df_sh.info())#查看交易数据概览信息
print(df_sh.axes)# 查看行和列的轴标签

df_sh.index = pd.to_datetime(df_sh.index)
df_sh.sort_index(inplace=True)
print(df_sh.axes)# 查看行和列的轴标签

#get_hist_data 未返回2008年数据
df_sh=ts.get_hist_data('sh',start='2008-01-01',end=datetime.datetime.now().strftime('%Y-%m-%d'))
print(df_sh.head())

#get_k_data 返回2008年数据
df_sh=ts.get_k_data('sh',start='2008-01-01',end=datetime.datetime.now().strftime('%Y-%m-%d'))
# print(df_sh.head())

df_sh.index = pd.to_datetime(df_sh.date)
df_sh.drop(axis=1, columns='date', inplace=True)
print(df_sh.head())


import sys
print(sys.path)
from utils import get_tushare_token

token = get_tushare_token()

print(token)

pro = ts.pro_api(token)#初始化pro接口
#获取平安银行日行情数据
pa=pro.daily(ts_code='000001.SZ', start_date='20180101',
               end_date='20190101')

print(pa.head())







