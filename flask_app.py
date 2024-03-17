# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"