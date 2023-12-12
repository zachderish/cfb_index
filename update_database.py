import mysql.connector, config
import GetRecruitingClass

#create recruiting databases
mydb = mysql.connector.connect(
  host="localhost",
  user="zderish",
  password=config.PASS,
  database="mydatabase"
)


mycursor = mydb.cursor(dictionary=True)
'''
sql = "INSERT INTO recruiting (year, top_player, top_team) VALUES (%s, %s, %s)"
val = [
  ("2018", "Trevor Lawrence", "Georgia")
]
mycursor.executemany(sql, val)

mydb.commit()
'''
'''
#print table contents
table_name = "recruiting2024"

mycursor.execute("SELECT * FROM recruiting2010")

results = mycursor.fetchall()

for row in results:
    print(row)
'''

#update table data
current_year = 2024
print("calling" + str(current_year))
recruiting_class = GetRecruitingClass.get_class(current_year)
sql = "INSERT INTO recruiting" + str(current_year) + " (name, position, ranking, stars, height, weight, school) VALUES (%s, %s, %s, %s, %s, %s, %s)"
mycursor.executemany(sql, recruiting_class)

mydb.commit()