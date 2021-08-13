from flask import render_template
from flask_mail import Message
from crypto import app
from crypto.services.mail import MailController
from crypto.services.sympol.main import sympolController as sym



mailController = MailController(app)
mailController.setConfig()


@app.route("/send-email-example")
def index():
    try:
        resources = [
            {
                'name': 'Etherum',
                'price': 1300
            },
            {
                'name': 'BTC',
                'price': 55000
            },
            {
                'name': 'DOGE',
                'price': 2
            },
        ]
        msg = Message('Hello from the other side!',
                    #   sender='amrtaher1995@gmail.com', recipients=['amrtaher1995@gmail.com', 'yar2nman@gmail.com'])
                      sender='amrtaher1995@gmail.com', recipients=['yar2nman@gmail.com'])
        msg.html = render_template('mail-template.html', resources=resources)
        msg.body = "Hello Crypto"
        mailController.sendMessage(msg)
    except Exception as e:
        print(e)
        return str(e)
    return "Message sent!"


@app.route('/')
def hello():
    return 'Hello World! from Ahmed'


@app.route('/html')
def html():
    return render_template('mail-template.html', resources=[
        {
            'name': 'Etherum',
            'price': 1300
        },
        {
            'name': 'BTC',
            'price': 55000
        },
        {
            'name': 'DOGE',
            'price': 2
        },
    ])

# return DataFrame showing sympol movement
@app.route("/sympolinfo/<sympol>")
def sympolinfo(sympol='MSFT'):
    try:
        msyminfo = sym(sympol).getSympolInfo()
        return msyminfo
    except:
        return 'Error'

# return Chart showing sympol movement        
@app.route('/sympolchart/<sympol>')
def sympolchart(sympol='MSFT'):
    try:
        mysymdata=sym(sympol).getSympolChart()
        return f"<img src='data:image/png;base64,{mysymdata}'/>"
    except:
        return 'Error'


# return Sympol metadata
@app.route("/sympoldf/<sympol>")
def sympoldf(sympol='MSFT'):
    try:
        df = sym(sympol).getSympolDataFrame()
        return {'data': df.to_json(), 'status': 200, 'message': f'Sympol: {sympol}'}
    except:
        return 'Error'