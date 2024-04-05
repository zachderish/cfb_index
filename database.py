import mysql.connector, config
import GetRecruitingClass
import GetTeamInfo
import json

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

class Player_Recruiting_2024(db.Model):

    __tablename__ = "player_recruiting_2024"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    pos = db.Column(db.String(5))
    ranking = db.Column(db.Integer())


'''
#create recruiting databases
mydb = mysql.connector.connect(
  host="localhost",
  user="zderish",
  password=config.PASS,
  database="mydatabase"
)
mycursor = mydb.cursor()

current_year = 2023
print("calling" + str(current_year))
recruiting_class = GetRecruitingClass.get_class_teams(current_year)
print(recruiting_class)
sql = "INSERT INTO team" + str(current_year) + " (ranking, team, points) VALUES (%s, %s, %s)"
mycursor.executemany(sql, recruiting_class)



year = 2023
while year >= 2010:
  print("calling" + str(year))
  team_records = GetTeamInfo.get_team_records(year)
  print(team_records)
  sql = "INSERT INTO records" + str(year) + " (team_id, year, team, conference, division, total_games, total_wins, total_losses, total_ties, conference_games, conference_wins, conference_losses, conference_ties) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor.executemany(sql, team_records)
  year -= 1


year = 2023
while year >= 2010:
  sql = "CREATE TABLE records" + str(year) + "(team_id VARCHAR(255), year VARCHAR(255), team VARCHAR(255), conference VARCHAR(255), division VARCHAR(255), total_games VARCHAR(255), total_wins VARCHAR(255), total_losses VARCHAR(255), total_ties VARCHAR(255), conference_games VARCHAR(255), conference_wins VARCHAR(255), conference_losses VARCHAR(255), conference_ties VARCHAR(255))"
  mycursor.execute(sql)
  year -= 1


mycursor.execute("SHOW TABLES")

result = mycursor.fetchall()
for x in result:
    print(x)

mydb.commit()
'''