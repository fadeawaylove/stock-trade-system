import akshare as ak 

# 实时行情数据接口:
# stock_df = ak.stock_zh_a_spot()
# print(stock_df)

# 历史行情数据接口：
stock_df = ak.stock_zh_a_daily(symbol="sh600000")
print(stock_df)




