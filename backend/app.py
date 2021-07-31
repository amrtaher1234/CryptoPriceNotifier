from flask import Flask, render_template
from services.mail import MailController
from flask_mail import Message

import base64
from io import BytesIO
from matplotlib.figure import Figure

import yfinance as yf

app = Flask(__name__)
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
                      sender='amrtaher1995@gmail.com', recipients=['amrtaher1995@gmail.com', 'yar2nman@gmail.com'])
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


# return chart showing stock movement
@app.route("/sympol/<sympol>")
def sympol(sympol='MSFT'):
    try:
        print('')
        df = yf.download(sympol)
        return df[-1:-5].to_html(classes='table table-striped')
    except:
        return 'Error'
        

