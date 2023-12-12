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
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM recruiting2023")

result = mycursor.fetchall()
for x in result:
    print(x)