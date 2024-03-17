# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="zderish",
    password=config.DB_PASS,
    hostname="zderish.mysql.pythonanywhere-services.com",
    databasename="zderish$cfb",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return "Hello"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"