from flask import render_template
from flask_mail import Message
from crypto import app
from crypto.services.mail import MailController

import base64
from io import BytesIO
from matplotlib.figure import Figure

import matplotlib.pylab as plt

import yfinance as yf

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


@app.route("/image")
def image():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


# return DataFrame showing sympol movement
@app.route("/sympol/<sympol>")
def sympol(sympol='MSFT'):
    try:
        print('')
        df = yf.download(sympol)
        return df[-1:-5].to_html(classes='table table-striped')
    except:
        return 'Error'

# return Chart showing sympol movement        
@app.route('/sympolechart/<sympol>')
def sympolechart(sympol='MSFT'):
    try:
        print('')
        plt.switch_backend('agg')
        df = yf.Ticker(sympol)
        fig = df.history(periods='1y', frequency='1').Open.plot(figsize=(10, 6)).get_figure()
        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return f"<img src='data:image/png;base64,{data}'/>"
    except:
        return 'Error'


# return Sympol metadata
@app.route("/sympol/<sympol>/metadata")
def sympolmetadata(sympol='MSFT'):
    try:
        print('')
        df = yf.Ticker(sympol).get_info()
        return {'data': df, 'status': 200, 'message': f'Sympol {sympol}'}
    except:
        return 'Error'