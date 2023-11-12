from flask import Flask, redirect, url_for
import search_database

app = Flask(__name__)

@app.route('/recruiting/year=<year>')
def year_recruiting(year):
   return search_database.table_data(year)

@app.route('/recruiting/year=<year>/team=<team>')
def team_recruiting(year, team):
   return search_database.team_data(year, team)

@app.route('/recruiting/year=<year>/position=<position>')
def position_recruiting(year, position):
   return search_database.position_data(year, position)

if __name__ == '__main__':
   app.run(debug = True)