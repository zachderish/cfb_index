import cfbd, config, sys, mysql.connector
from cfbd.rest import ApiException


#Connect to database
mydb = mysql.connector.connect(
  host="cfb-database.cxwmm2qoadf6.us-east-1.rds.amazonaws.com",
  user="admin",
  password=config.PASS,
  database="cfb"
)


# Configure API key authorization: ApiKeyAuth
CONFIGURATION = cfbd.Configuration()
CONFIGURATION.api_key['Authorization'] = config.API_KEY
CONFIGURATION.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.RecruitingApi(cfbd.ApiClient(CONFIGURATION))

def append_data_player(player, data):
    player.append(data.id)
    player.append(data.athlete_id)
    player.append(data.recruit_type)
    player.append(data.year)
    player.append(data.ranking)
    player.append(data.name)
    player.append(data.school)
    player.append(data.committed_to)
    player.append(data.position)
    player.append(data.height)
    player.append(data.weight)
    player.append(data.stars)
    player.append(data.rating)
    player.append(data.city)
    player.append(data.state_province)
    player.append(data.country)
    player.append(data.hometown_info.latitude)
    player.append(data.hometown_info.longitude)
    player.append(data.hometown_info.county_fips)
    return player

def append_data_team(team, data):
    team.append(data.year)
    team.append(data.rank)
    team.append(data.team)
    team.append(data.points)
    return team

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

    mycursor.execute("CREATE TABLE recruiting" + str(year) + " (id INT, athleteId INT, recruitType VARCHAR(25), year INT, ranking INT, name VARCHAR (50), school VARCHAR(50), committedTo VARCHAR(50), position VARCHAR(10), height DOUBLE, weight DOUBLE, stars INT, rating DOUBLE, city VARCHAR(50), stateProvince VARCHAR(20), country VARCHAR(20), latitude DOUBLE, longitude DOUBLE, countyFips VARCHAR(10))")

    print("calling" + str(year))
    recruiting_class = get_class(year)
    sql = "INSERT INTO recruiting" + str(year) + " (id, athleteId, recruitType, year, ranking, name, school, committedTo, position, height, weight, stars, rating, city, stateProvince, country, latitude, longitude, countyFips) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, recruiting_class)

    mydb.commit()

def get_team_recruiting():

    teams = []
    try:
        # Team recruiting ratings and rankings
        api_response = api_instance.get_recruiting_teams()
    
        for data in api_response:
            team = []
            team = append_data_team(team, data)

            teams.append(team)
        return teams

    except ApiException as e:
        print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)

def update_team_recruiting():
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("DROP TABLE teamRecruiting;")

    mycursor.execute("CREATE TABLE teamRecruiting (year INT, teamRank INT, team VARCHAR(25), points FLOAT, PRIMARY KEY (year, team));")

    print("calling teamRecruiting")
    recruiting_data = get_team_recruiting()
    sql = "INSERT IGNORE INTO teamRecruiting (year, teamRank, team, points) VALUES (%s, %s, %s, %s);"
    mycursor.executemany(sql, recruiting_data)

    mydb.commit()

if  __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "players":
        year = sys.argv[2]
        update_class(int(year))
    else:
        update_team_recruiting()
