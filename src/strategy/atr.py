import talib


def atr(data, period):
    return talib.ATR(data.High.values, data.Low.values, data.Close.values, timeperiod=period)
