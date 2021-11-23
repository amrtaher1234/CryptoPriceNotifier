import io
from matplotlib.pyplot import title
from pandas.core.frame import DataFrame
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from io import BytesIO
import numpy as np

import base64
from matplotlib.figure import Figure

import matplotlib.pylab as plt

class symbolController():
    def __init__(self, symbol='MSFT', period='10y', interval='1d'):
        self.symbol = symbol
        try:
            self.df = pd.read_csv(f'{symbol}.csv', index_col=0)
            self.df.index = pd.to_datetime(self.df.index)

        except:
            self.df = yf.download(self.symbol, period=period, interval=interval)
            # calculate the mean for a window of 20 days 'Simple Moving Avarage'
            self.df['SMA'] = self.df['Close'].rolling(window=20).mean()
            self.df['SMA50'] = self.df['Close'].rolling(window=50).mean()
            self.df['standardeviation'] = self.df['Close'].rolling(window=20).std()

            # calculate upper limit and lower limit
            self.df['upper'] = self.df['SMA'] + self.df['standardeviation'] *2
            self.df['lower'] = self.df['SMA'] - self.df['standardeviation'] *2

            # add buy and sell signals at each point the close moves beyound the limit
            self.df['buy_signal'] = np.where(self.df['Close'] < self.df['lower'], True, False)
            self.df['Sell_signal'] = np.where(self.df['upper'] < self.df['Close'], True, False)

            # Calculating RSI
            self.df['diff'] = self.df['Close'].diff(1)
            self.df['gain'] = self.df['diff'].clip(lower=0).round(2)
            self.df['loss'] = self.df['diff'].clip(upper=0).abs().round(2)

            # self.df.rsi(close='price', length=14, append=True)
            self.df['rsi_14'] = ta.rsi(close=self.df['Close'], length=14)

            


            self.df.to_csv(f'{symbol}.csv')

    def getsymbolInfo(self):
         try:
            ticker = yf.Ticker(self.symbol)
            dfx = ticker.get_info()
            return {'data': dfx, 'status': 200, 'message': f'symbol {self.symbol}'}
         except:
            return 'Error'

    def getSymbolHistoryChart(self):
        try:
            
            plt.switch_backend('agg')
            fig = self.df.Open\
                .plot(figsize=(12, 6), color='blue', title=f'{str.upper(self.symbol)} History Chart', ylabel='Price U$')\
                .get_figure()
            return fig       
        except:
            return 'Error'

    def getSymbolTopButtomCreossChart(self):
        self.df.dropna(inplace=True)
        mf = self.df.iloc[-366:]
        plt.figure(figsize=(18, 9))
        plt.plot(mf[['upper', 'lower', 'Close', 'SMA']])
        plt.fill_between(mf.index, mf.lower, mf.upper, color='blue', alpha=0.05)
        plt.legend(['upper', 'lower', 'Close', 'SMA'])
        plt.scatter(mf.index[mf.buy_signal], mf[mf.buy_signal].Close, marker='^', c='green' )
        plt.scatter(mf.index[mf.Sell_signal], mf[mf.Sell_signal].Close, marker='^', c='red')
        plt.grid(which='both')
        bytes_image = io.BytesIO()
        plt.xlabel('Date')
        plt.ylabel('Close Price in U$')
        plt.title(f'{str.upper(self.symbol)} Top Buttom Cross Chart')
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image

    def getSymbolShortLongSMAChart(self):
        self.df.dropna(inplace=True)
        mf = self.df.iloc[-366:]
        plt.figure(figsize=(18, 9))
        plt.plot(mf[['Close', 'SMA', 'SMA50']])
        plt.grid(b=True, which='both')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.title(f'{str.upper(self.symbol)} Short Long Moving Avarage Chart')
        
        # plt.fill_between(mf.index, mf.lower, mf.upper, color='blue', alpha=0.05)
        plt.legend(['Close', 'SMA', 'SMA50'])
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        return bytes_image



    def getsymbolDataFrame(self):
        try:
            return self.df
        except:
            return 'Error'
