from flask import  Blueprint, render_template
from crypto.services.symbol.main import symbolController as sym

from flask_mail import Message
from crypto import app
from crypto.services.mail import MailController

main = Blueprint('main', __name__)

mailController = MailController(app)
mailController.setConfig()


@main.route("/send-email-example")
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


@main.route('/')
def hello():
    return 'Hello World! from Ahmed'


@main.route('/html')
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

