import mysql.connector, config
import GetRecruitingClass
import json

#create recruiting databases
mydb = mysql.connector.connect(
  host="localhost",
  user="zderish",
  password=config.PASS,
  database="mydatabase"
)

mycursor = mydb.cursor(dictionary=True)

# get general overview of recruiting years
def recruiting_data():
  # get table data
  mycursor.execute("SELECT * FROM recruiting")
  data = mycursor.fetchall()
  json_data = json.dumps(data)
  return json_data

# get general team data given a year
def recruiting_teams(year):
  mycursor.execute("SELECT * FROM team%s", (int(year),))
  data = mycursor.fetchall()
  json_data = json.dumps(data)
  return json_data

def table_data(year):
  # get table data
  mycursor.execute("SELECT * FROM recruiting%s", (int(year),))
  data = mycursor.fetchall()
  json_data = json.dumps(data)
  return json_data

def team_data(year, team):
  mycursor.execute("SELECT * FROM recruiting%s WHERE school = %s", (int(year), team))
  data = mycursor.fetchall()
  json_data = json.dumps(data)
  return json_data

def position_data(year, position):
  mycursor.execute("SELECT * FROM recruiting%s WHERE position = %s", (int(year), position))
  data = mycursor.fetchall()
  json_data = json.dumps(data)
  return json_data

'''
recruiting_class = GetRecruitingClass.get_class(2024)
sql = "INSERT INTO recruiting24 (name, position, ranking, stars, height, weight, school) VALUES (%s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(sql, recruiting_class)

mydb.commit()
'''
'''
earliestYear = 2000
currentYear = 2024
while earliestYear <= currentYear:
    recruiting_class = GetRecruitingClass.get_class(earliestYear)
    print(recruiting_class)
    earliestYear += 1
'''