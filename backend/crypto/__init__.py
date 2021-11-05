from flask import Flask
from .services.mail import MailController


app = Flask(__name__)
mailController = MailController(app)
mailController.setConfig()

# from crypto import routes

from crypto.symbol.routes import symbol
from crypto.main.routers import main
app.register_blueprint(symbol)
app.register_blueprint(main)
