import time

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World! I have'



@app.route('/test')
def test():
    print(request.args)
    return 'Dies in the testing phase.'
