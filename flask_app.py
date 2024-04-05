# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import mysql.connector, config
import config

app = Flask(__name__)



mydb = mysql.connector.connect(
  host="zderish.mysql.pythonanywhere-services.com",
  user="zderish",
  password=config.DB_PASS,
  database="zderish$cfb"
)

mycursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM comments")
data = mycursor.fetchall()

@app.route('/')
def hello_world():
    return f"Hello {data}"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"

