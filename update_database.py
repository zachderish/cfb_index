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
#print table contents
table_name = "team2023"

mycursor.execute("SELECT * FROM " + table_name)

results = mycursor.fetchall()

for row in results:
    print(row)
'''

'''
#update table data
current_year = 2024

mycursor.execute("DROP TABLE recruiting" + str(current_year))

mycursor.execute("CREATE TABLE recruiting" + str(current_year) + " (name VARCHAR(255), position VARCHAR(255), ranking VARCHAR(255), stars VARCHAR(255), height VARCHAR(255), weight VARCHAR(255), school VARCHAR(255))")

print("calling" + str(current_year))
recruiting_class = GetRecruitingClass.get_class(current_year)
sql = "INSERT INTO recruiting" + str(current_year) + " (name, position, ranking, stars, height, weight, school) VALUES (%s, %s, %s, %s, %s, %s, %s)"
mycursor.executemany(sql, recruiting_class)

mydb.commit()
'''