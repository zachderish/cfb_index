from flask import Flask, redirect, url_for, make_response
import search_database

app = Flask(__name__)

'''
@app.route('/records/year=<year>')
def records(year):
   data = search_database.records(year)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response

@app.route('/records/team=<team>')
def records_teams(team):
   data = search_database.records_team(team)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response   

@app.route('/records/team=<team>/year=<year>')
def records_team_year(team, year):
   data = search_database.records_team_year(team, year)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response


@app.route('/recruiting')
def recruiting():
   data = search_database.recruiting_data()
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response

@app.route('/recruiting/teams/year=<year>')
def recruiting_teams(year):
   data = search_database.recruiting_teams(year)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response

@app.route('/recruiting/year=<year>')
def year_recruiting(year):
   data = search_database.table_data(year)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response

@app.route('/recruiting/year=<year>/team=<team>')
def team_recruiting(year, team):
   data = search_database.team_data(year, team)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response

@app.route('/recruiting/year=<year>/position=<position>')
def position_recruiting(year, position):
   data = search_database.position_data(year, position)
   response = make_response(data)
   response.headers['Access-Control-Allow-Origin'] = '*'
   return response
'''