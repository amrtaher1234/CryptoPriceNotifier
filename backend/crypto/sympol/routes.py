from flask import  Blueprint
from crypto.services.sympol.main import sympolController as sym


sympol = Blueprint('sympol', __name__)

# return DataFrame showing sympol movement
@sympol.route("/sympol/info/<sympol>")
def sympolinfo(sympol='MSFT'):
    try:
        msyminfo = sym(sympol).getSympolInfo()
        return msyminfo
    except:
        return 'Error'

# return Chart showing sympol movement        
@sympol.route('/sympol/chart/<sympol>')
def sympolchart(sympol='MSFT'):
    try:
        mysymdata=sym(sympol).getSympolChart()
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'


# return Sympol metadata
@sympol.route("/sympol/df/<sympol>")
def sympoldf(sympol='MSFT'):
    try:
        df = sym(sympol).getSympolDataFrame()
        return {'data': df.to_json(), 'status': 200, 'message': f'Sympol: {sympol}'}
    except:
        return 'Error'