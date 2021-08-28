import os
from .base import BaseMailController
from flask import Flask
from flask_mail import Mail, Message


class MailConfig:
    def __init__(self, mailService: str, username: str, password: str):
        self.mailService = mailService
        self.username = username
        self.password = password


class MailController(BaseMailController):
    def __init__(self, app: Flask):
        self.mail = None
        self.app = app

    def setConfig(self, config: MailConfig = None):
        if config is None:
            config = MailConfig('smtp.gmail.com', os.environ.get(
                'EMAIL_USER'), os.environ.get('EMAIL_PASS'))
        self.app.config['MAIL_SERVER'] = config.mailService
        self.app.config['MAIL_PORT'] = 465
        self.app.config['MAIL_USERNAME'] = config.username
        self.app.config['MAIL_PASSWORD'] = config.password
        self.app.config['MAIL_USE_TLS'] = False
        self.app.config['MAIL_USE_SSL'] = True
        self.mail = Mail(self.app)

    def sendMessage(self, msg: Message):
        msg.sender = msg.sender or self.username
        self.mail.send(msg)

def msendemail():
    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email='yar2nman@gmail.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
