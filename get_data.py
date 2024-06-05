import cfbd
import sys
import mysql.connector
from cfbd.rest import ApiException

sys.path.append('../config')

#Connect to database
mydb = mysql.connector.connect(
  host="cfb-database.cxwmm2qoadf6.us-east-1.rds.amazonaws.com",
  user="admin",
  password=sys.config.PASS,
  database="cfb"
)


# Configure API key authorization: ApiKeyAuth
CONFIGURATION = cfbd.Configuration()
CONFIGURATION.api_key['Authorization'] = sys.config.API_KEY
CONFIGURATION.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RecruitingApi(cfbd.ApiClient(CONFIGURATION))

def append_data_player(player, data):
    player.append(data.name)
    player.append(data.position), 
    player.append(data.ranking), 
    player.append(data.stars)
    player.append(data.height)
    player.append(data.weight)
    player.append(data.committed_to)
    return player

def get_class(year):
    year = year # int | Recruiting class year (required if team no specified) (optional)
    classification = 'HighSchool' # str | Type of recruit (HighSchool, JUCO, PrepSchool) (optional) (default to HighSchool)
    position = 'position_example' # str | Position abbreviation filter (optional)
    state = 'state_example' # str | State or province abbreviation filter (optional)
    team = 'team_example' # str | Committed team filter (required if year not specified) (optional)

    players = []
    try:
        # Player recruiting ratings and rankings
        api_response = api_instance.get_recruiting_players(year=year)
        #pprint(api_response)

        for data in api_response:
            player = []
            player = append_data_player(player, data)
            players.append(player)
        return players

    except ApiException as e:
        print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)

def update_class(year):
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("DROP TABLE recruiting" + str(year))

    mycursor.execute("CREATE TABLE recruiting" + str(year) + " (name VARCHAR(255), position VARCHAR(255), ranking VARCHAR(255), stars VARCHAR(255), height VARCHAR(255), weight VARCHAR(255), school VARCHAR(255))")

    print("calling" + str(year))
    recruiting_class = get_class(year)
    sql = "INSERT INTO recruiting" + str(year) + " (name, position, ranking, stars, height, weight, school) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, recruiting_class)

    mydb.commit()

if  __name__ == "__main__":
    year = sys.argv[1]
    update_class(int(year))
