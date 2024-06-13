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
    return 'Endpoint: recruiting/year=<year>'

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

@app.route('recruiting/year=<year>/team=<team>')
def team_recruiting(year, team):
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM recruiting" + year + " WHERE team = " + team
    mycursor.execute(query)
    data = mycursor.fetchall()
    json_data = json.dumps(data)
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run()
