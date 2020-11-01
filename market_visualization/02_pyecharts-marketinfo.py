import datetime
import pandas_datareader.data as web

# Overlap+Grid方法绘制交易行情界面
from pyecharts.charts import Grid, Line, Bar, EffectScatter, Kline  # newest 1.7.0
from pyecharts import options as opts

# example1 senior quotations
df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.date.today())
df_stockload['Ma20'] = df_stockload.Close.rolling(
    window=20).mean()  # pd.rolling_mean(df_stockload.Close,window=20)
df_stockload['Ma30'] = df_stockload.Close.rolling(
    window=30).mean()  # pd.rolling_mean(df_stockload.Close,window=30)
df_stockload['Ma60'] = df_stockload.Close.rolling(
    window=60).mean()  # pd.rolling_mean(df_stockload.Close,window=60)

volume_rise = [df_stockload.Volume[x] if df_stockload.Close[x] > df_stockload.Open[x] else "0" for x in
               range(0, len(df_stockload.index))]
volume_drop = [df_stockload.Volume[x] if df_stockload.Close[x] <= df_stockload.Open[x] else "0" for x in
               range(0, len(df_stockload.index))]

ohlc = list(zip(df_stockload.Open, df_stockload.Close, df_stockload.Low, df_stockload.High))
dates = df_stockload.index.strftime('%Y-%m-%d')

kline = (
    Kline()
    .add_xaxis(dates.tolist())
    .add_yaxis(
        "kline",
        ohlc,
        markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_="max", value_dim="close")] # 标注最大值线
        ),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True, is_show=False),
        yaxis_opts=opts.AxisOpts(is_scale=True,
        splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            )
        ),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="20%", pos_right="0%"), # 调整图例的位置
        title_opts=opts.TitleOpts(title="行情显示图"),
    )

)

line = (
    Line()
        .add_xaxis(dates.tolist())
        .add_yaxis("Ma20", df_stockload["Ma20"].tolist())
        .add_yaxis("Ma30", df_stockload["Ma30"].tolist())
        .add_yaxis("Ma60", df_stockload["Ma60"].tolist())
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)

bar = (
    Bar()
        .add_xaxis(dates.tolist())
        .add_yaxis("rvolume", volume_rise, stack="stack1", category_gap="50%") # 堆积柱形图
        .add_yaxis("dvolume", volume_drop, stack="stack1", category_gap="50%") # 堆积柱形图
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        #xaxis_index=[0, 1] 同时显示两幅图
        .set_global_opts(datazoom_opts=[opts.DataZoomOpts(xaxis_index=[0,1], is_show= True)], # 图表数据缩放
                         legend_opts=opts.LegendOpts(orient="vertical", pos_right="0%")

        )
)

overlap_1 = kline.overlap(line)

grid = (
    Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_top="60%"), grid_index=0)
        .add(overlap_1, grid_opts=opts.GridOpts(pos_bottom="40%"), grid_index=1)
        .render(r"grid_vertical.html") # raw string 非转义 string
)