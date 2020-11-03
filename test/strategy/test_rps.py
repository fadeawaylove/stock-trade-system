import tushare as ts
import pandas as pd
from strategy import show_rps

token = '08bacc25245b55f5bd2307c655af42431fe3c731080bd1750858489b'
# 初始化pro接口
pro = ts.pro_api(token)
# 查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

code_list = list(data.ts_code)[:10]
code_list.append("600873.SZ")

def get_one(code):
    start = "20181001"
    end = "20200401"
    code_data = pro.daily(ts_code=code, start_date=start, end_date=end)
    code_data.fillna(method='bfill', inplace=True)  # 后一个数据填充NAN1
    code_data.index = pd.to_datetime(code_data.trade_date)
    code_data.sort_index(inplace=True)
    code_data.drop(axis=1, columns='trade_date', inplace=True)
    return code_data


st_data = pd.DataFrame({d: get_one(d).close for d in code_list}, columns=code_list)

show_rps(st_data, 250, show=True, start_index="20200101")
