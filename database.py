import mysql.connector, config
import GetRecruitingClass
import GetTeamInfo
import json

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

'''
current_year = 2023
conference = "ACC"
print("calling" + str(current_year))
recruiting_class = GetTeamInfo.get_team_records(current_year, conference)
print(recruiting_class)
sql = "INSERT INTO team" + str(current_year) + " (ranking, team, points) VALUES (%s, %s, %s)"
mycursor.executemany(sql, recruiting_class)

mycursor.execute("SHOW TABLES")
'''

result = mycursor.fetchall()
for x in result:
    print(x)

mydb.commit()