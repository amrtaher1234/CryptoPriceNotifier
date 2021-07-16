from flask import Flask, render_template
from services.mail.mail import MailController
from flask_mail import Message


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
    return 'Hello World!'


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
