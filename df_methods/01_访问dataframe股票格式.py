import datetime
import pandas_datareader.data as web


df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2018, 2, 1))

print(df_stockload.head(10))
print(df_stockload.index)  # see the index
print(df_stockload.columns)  # see the columns
print(df_stockload.axes)  # see index and columns

print(df_stockloado.values)  # see all the values
print(type(df_stockload.values))  # <class 'numpy.ndarray'>

print(df_stockload['Open'])  # see the column Open
print(type(df_stockload['Open']))  # <class 'pandas.core.series.Series'>

print(df_stockloads[0:1])  # slice to see several columns data
print(type(df_stockload[0:1]))  # <class 'pandas.core.frame.DataFrame'>

# loc
print(df_stockloadtoc.loc['2018-01-02'])
print(df_stockload.loc['2018-01-02',['High','Low']])


# iloc
print(df_stockload.iloc[[0,2],[0,1]])
print(df_stockload.iloc[0:2, 0:1])
print(df_stockload.iloc[0:2])

# ix 即将弃用
print(df_stockload.ix[[0,2], 'High'])

# transform
print(df_stockload.iloc[[0,2], df_stockload.columns.get_loc('High')])

print(df_stockload.iloc[[0,2], df_stockload.columns.get_indexer(['High', 'Open'])])

df_stockload.loc[['2018-01-02', '2018-01-04'], ['High','Open']]
"""
KeyError: "None of [Index(['2018-01-02', '2018-01-04'], dtype='object', name='Date')] are in the [index]"
"""
print(df_stockload.loc[[pd.to_datetime('2018-01-02'), pd.to_datetime('2018-01-04')], ['High','Open']])


























