import mysql.connector, config
import GetRecruitingClass

#create recruiting databases
mydb = mysql.connector.connect(
  host="localhost",
  user="zderish",
  password=config.PASS,
  database="mydatabase"
)

def table_data():
  # get table data
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM recruiting24")
  data = mycursor.fetchall()

  return data

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