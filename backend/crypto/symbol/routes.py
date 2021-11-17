
import io
from flask import  Blueprint, render_template, send_file, Response

from crypto.services.symbol.main import symbolController as sym
from flask_cors import cross_origin
import json

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


symbol = Blueprint('symbol', __name__)

# return DataFrame showing symbol Information
@symbol.route("/symbol/info/<symbol>")
@cross_origin()
def symbolinfo(symbol='MSFT'):
    try:
        msyminfo = sym(symbol).getsymbolInfo()
        return msyminfo
    except:
        return 'Error'

# return Chart showing symbol movement
@symbol.route('/symbol/chart/<symbol>')
@cross_origin()
def symbolchart(symbol='MSFT'):
    try:
        fig=sym(symbol).getSymbolHistoryChart()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    except Exception as e:
        return e

# html to test the chart returned from symbol/chart/symbol
@symbol.route('/symbol/html/<symbol>')
@cross_origin()
def symbolcharthtml(symbol='MSFT'):
    try:
        return "<div>"\
                f"<img src='/symbol/chart/{symbol}'/></div>"\
                "<div>Hi</div>"
    except Exception as e:
        return e


# return Chart showing symbol movement including top, buttom, SMA
@symbol.route('/symbol/tbsignalchart/<symbol>')
@cross_origin()
def symboltbchart(symbol='MSFT'):
    try:
        bytes_obj=sym(symbol).getSymbolTopButtomCreossChart()
    
        return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
        # output = io.BytesIO()
        # FigureCanvas(fig).print_png(output)
        # return Response(output.getvalue(), mimetype='image/png')
    except Exception as e:
        return e

# return Chart showing symbol movement including top, buttom, SMA
@symbol.route('/symbol/longshortsmachart/<symbol>')
@cross_origin()
def symboltbchartshortlong(symbol='MSFT'):
    try:
        bytes_obj=sym(symbol).getSymbolShortLongSMAChart()
    
        return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
    except Exception as e:
        return e



def msymbolchart(symbol='MSFT'):
    try:
        mysymdata=sym(symbol).getSymbolHistoryChart()
        return mysymdata
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'

# return symbol DataFrame
@symbol.route("/symbol/df/<symbol>")
@cross_origin()
def symboldf(symbol='MSFT'):
    try:
        df = sym(symbol).getsymbolDataFrame()
        return {'data': df.to_json(), 'status': 200, 'message': f'symbol: {symbol}'}
    except:
        return 'Error'

@symbol.route("/symbol/page/<symbol>")
@cross_origin()
def symbolpage(symbol='MSFT'):
    try:
        resources = {}
        resources['symbol'] = symbol

        msym = json.loads(symbolinfo(symbol).data)['data']
        short_name = msym['shortName']
        long_name = msym['longName']

        resources['name'] = f'{short_name} / {long_name}'
        resources['price'] = msym['currentPrice']


        # myrc = msymbolchart(symbol)

        return render_template('web-template.html', resources=resources)

    except:
        return 'Error'