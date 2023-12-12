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

sql = "INSERT INTO recruiting (year, top_player, top_team) VALUES (%s, %s, %s)"
val = [
  ("2017", "Jaelan Philips", "Alabama"),
  ("2016", "Rashan Gary", "Alabama"),
  ("2015", "Trenton Thompson", "Alabama"),
  ("2014", "Leonard Fournette", "Alabama"),
  ("2013", "Robert Nkemdiche", "Alabama"),
  ("2012", "Dorial Green-Beckham", "Alabama"),
  ("2011", "Jadeveon Clowney", "Alabama"),
  ("2010", "Ronald Powell", "Florida"),
  ("2009", "Matt Barkley", "LSU"),
  ("2008", "Da'Quan Bowers", "Miami"),
  ("2007", "Joe McKnight", "Florida"),
  ("2006", "Andre Smith", "USC"),
  ("2005", "Eugene Monroe", "USC"),
  ("2004", "Adrian Peterson", "Florida State"),
  ("2003", "Ernie Sims", "Florida"),
  ("2002", "Vince Young", "Texas"),
  ("2001", "Kevin Jones", "Florida State"),
  ("2000", "D.J. Williams", "Tennessee")
]
mycursor.executemany(sql, val)

mydb.commit()


#print table contents
table_name = "recruiting"

mycursor.execute("SELECT * FROM " + table_name)

results = mycursor.fetchall()

for row in results:
    print(row)


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