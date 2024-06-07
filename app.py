from flask import Flask, redirect, url_for, make_response
import mysql.connector, config, json

app = Flask(__name__)


#Connect to database
mydb = mysql.connector.connect(
  host="cfb-database.cxwmm2qoadf6.us-east-1.rds.amazonaws.com",
  user="admin",
  password=config.PASS,
  database="cfb"
)

@app.route('/')
def hello_world():
    return 'This is a test 1.'

@app.route('/path1')
def hello_path1():
    return f"Hello test path1!"

@app.route('/path2')
def hello_path2():
    return "Hello test path2!"

@app.route('/recruiting/year=<year>')
def player_recruiting(year):
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM recruiting" + year
    mycursor.execute(query)
    data = mycursor.fetchall()
    json_data = json.dumps(data)
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run()
