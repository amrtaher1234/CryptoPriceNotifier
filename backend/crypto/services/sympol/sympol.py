import yfinance as yf
from io import BytesIO

import base64
from matplotlib.figure import Figure

import matplotlib.pylab as plt

class sympolController():
    def __init__(self, sympol='MSFT'):
        self.sympol = sympol

    def getSymbolInfo(self):
         try:
            print('')
            df = yf.Ticker(self.sympol).get_info()
            return {'data': df, 'status': 200, 'message': f'Sympol {self.sympol}'}
         except:
            return 'Error'

    def getSympolChart(self):
        try:
            plt.switch_backend('agg')
            df = yf.Ticker(self.sympol)
            fig = df.history(periods='1y', frequency='1').Open.plot(figsize=(10, 6)).get_figure()
            buf = BytesIO()
            fig.savefig(buf, format="png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return data       
        except:
            return 'Error'

