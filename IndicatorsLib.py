import talib
import numpy as np
import pandas as pd


# print(talib.get_functions())
# print(talib.get_function_groups())


class TalibIndictor:
    """
        用TA-Lib封装更灵活的指标库
    """

    # Momentum Indicator Functions，动量指标函数
    @staticmethod
    def ADX_DF(dataframe: pd.DataFrame, N=14):
        res = talib.ADX(dataframe.high.values, dataframe.low.values, dataframe.close.values, N)
        return pd.DataFrame({'ADX': res}, index=dataframe.index)

    @staticmethod
    def ADXR_DF(DataFrame, N=14):
        # ADXR - Average Directional Movement Index Rating
        res = talib.ADXR(DataFrame.high.values, DataFrame.low.values, DataFrame.close.values, N)
        return pd.DataFrame({'ADXR': res}, index=DataFrame.index)

    @staticmethod
    def CMO(Series, timeperiod=14):
        # CMO - Chande Momentum Oscillator
        res = talib.CMO(Series.values, timeperiod)
        return pd.Series(res, index=Series.index)

    @staticmethod
    def MACD_SER(Series, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        # MACD - Moving Average Convergence/Divergence
        macd_dif, macd_dea, macd_bar = talib.MACD(
            Series.values, fastperiod, slowperiod, signalperiod)
        return pd.Series(macd_dif, index=Series.index), pd.Series(macd_dea, index=Series.index), pd.Series(macd_bar,
                                                                                                           index=Series.index)

    @staticmethod
    def STOCH_DF(DataFrame, fastkperiod=9, slowkperiod=3, slowkmatype=0, slowdperiod=3, slowdmatype=0):
        # STOCH - Stochastic
        K, D = talib.STOCH(DataFrame.high.values, DataFrame.low.values, DataFrame.close.values, \
                           fastkperiod, slowkperiod, slowkmatype, slowdperiod, slowdmatype)
        J = 3 * K - 2 * D
        return pd.Series(K, index=DataFrame.index), pd.Series(D, index=DataFrame.index), pd
