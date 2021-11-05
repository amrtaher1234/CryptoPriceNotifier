
from flask import  Blueprint, render_template

from crypto.services.symbol.main import symbolController as sym
from flask_cors import cross_origin
import json


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
        mysymdata=sym(symbol).getsymbolChart()
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'

def msymbolchart(symbol='MSFT'):
    try:
        mysymdata=sym(symbol).getsymbolChart()
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
        
        msym = json.loads(symbolinfo(symbol).data)['data']
        short_name = msym['shortName']
        long_name = msym['longName']

        resources['name'] = f'{short_name} / {long_name}'
        resources['price'] = msym['currentPrice']


        myrc = msymbolchart(symbol)
    
        return render_template('web-template.html', resources=resources, chart=myrc)

    except:
        return 'Error'