from flask import Flask
from .services.mail import MailController


app = Flask(__name__)
mailController = MailController(app)
mailController.setConfig()

from crypto import routes