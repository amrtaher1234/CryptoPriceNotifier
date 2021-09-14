from flask import Flask
from .services.mail import MailController


app = Flask(__name__)
mailController = MailController(app)
mailController.setConfig()

# from crypto import routes

from crypto.sympol.routes import sympol
from crypto.main.routers import main
app.register_blueprint(sympol)
app.register_blueprint(main)
