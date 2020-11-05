import os
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

from tqdm import tqdm

token = open("../../.tushare_token").read()

pro = ts.pro_api(token)


def get_all_stock_list(exclude_gem=True):
    """
    获取股票列表
    :param exclude_gem: True则排除创业板，False返回全部
    :return:
    """
    file_name = "stock_list_all_%s.csv" % datetime.datetime.today().strftime("%Y%m%d")
    file_path = '../data/%s' % file_name
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
    else:
        data = pro.stock_basic(exchange='', list_status='L',
                               fields='ts_code,symbol,name,area,fullname,enname,industry,market,list_status,list_date')
        data.to_csv(file_path)
    if exclude_gem:
        return data.loc[data["market"] != "科创板"]
    return data


def main():
    # 1.获取所有股票列表
    stock_list = get_all_stock_list().loc[range(10)]
    # 2.筛选出RPS值为前百分之二十的(只需要收盘价)
    stock_pct_data = pd.DataFrame()

    pct_file_path = "../data/stock_pct_data.csv"
    if os.path.exists(pct_file_path):
        stock_pct_data = pd.read_csv(pct_file_path, index_col='trade_date', parse_dates=True)
    else:
        for _, row in tqdm(stock_list.iterrows(), desc="获取中", total=len(stock_list), ):
            name = row["name"]
            stock_data = ts.pro_bar(ts_code=row["ts_code"], api=pro, adj='qfq', start_date='20200101',
                                    end_date=datetime.datetime.today().strftime("%Y%m%d"))

            stock_data.set_index('trade_date', inplace=True)
            stock_data.index = pd.to_datetime(stock_data.index)
            stock_data.sort_index(axis=0, ascending=True, inplace=True)

            # axis=0表示上下合并，1表示左右合并，ignore_index=True表示忽略原来的索引
            # stock_pct_data = pd.concat([stock_pct_data, stock_data[name]], axis=1)
            stock_pct_data[name] = stock_data.close.pct_change(5)
        stock_pct_data.to_csv(pct_file_path)

    # 排序
    sorted_data = pd.DataFrame(index=stock_pct_data.index, columns=list(range(1, 11)))
    for index, row in stock_pct_data.iterrows():
        x = row.sort_values(ascending=False)
        sorted_data.loc[index] = x.index

    print(sorted_data)


if __name__ == '__main__':
    main()
