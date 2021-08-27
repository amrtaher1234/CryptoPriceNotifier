
from flask import  Blueprint, render_template

from crypto.services.sympol.main import sympolController as sym
from flask_cors import cross_origin
import json


sympol = Blueprint('sympol', __name__)

# return DataFrame showing sympol Information
@sympol.route("/sympol/info/<sympol>")
@cross_origin()
def sympolinfo(sympol='MSFT'):
    try:
        msyminfo = sym(sympol).getSympolInfo()
        return msyminfo
    except:
        return 'Error'

# return Chart showing sympol movement        
@sympol.route('/sympol/chart/<sympol>')
@cross_origin()
def sympolchart(sympol='MSFT'):
    try:
        mysymdata=sym(sympol).getSympolChart()
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'

def msympolchart(sympol='MSFT'):
    try:
        mysymdata=sym(sympol).getSympolChart()
        return mysymdata
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'

# return Sympol DataFrame
@sympol.route("/sympol/df/<sympol>")
@cross_origin()
def sympoldf(sympol='MSFT'):
    try:
        df = sym(sympol).getSympolDataFrame()
        return {'data': df.to_json(), 'status': 200, 'message': f'Sympol: {sympol}'}
    except:
        return 'Error'

@sympol.route("/sympol/page/<sympol>")
@cross_origin()
def sympolpage(sympol='MSFT'):
    try:
        resources = {}
        
        msym = json.loads(sympolinfo(sympol).data)['data']
        short_name = msym['shortName']
        long_name = msym['longName']

        resources['name'] = f'{short_name} / {long_name}'
        resources['price'] = msym['currentPrice']


        myrc = msympolchart(sympol)
    
        return render_template('web-template.html', resources=resources, chart=myrc)

    except:
        return 'Error'