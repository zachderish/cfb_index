from flask import Flask, redirect, url_for
import database

app = Flask(__name__)

@app.route('/recruiting')
def recruiting():
   return database.table_data()

@app.route('/recruiting/team=<team>')
def team_recruiting(team):
   return database.team_data(team)

@app.route('/recruiting/position=<position>')
def position_recruiting(position):
   return database.position_data(position)

if __name__ == '__main__':
   app.run(debug = True)