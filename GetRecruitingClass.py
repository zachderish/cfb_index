import cfbd, config
from cfbd.rest import ApiException

# Configure API key authorization: ApiKeyAuth
CONFIGURATION = cfbd.Configuration()
CONFIGURATION.api_key['Authorization'] = config.API_KEY
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

def append_data_team(team, data):
    team.append(data.rank)
    team.append(data.team)
    team.append(data.points)
    return team

def get_class_teams(year):
    print(year)
    year = year # int | Recruiting class year (required if team no specified) (optional)
    classification = 'HighSchool' # str | Type of recruit (HighSchool, JUCO, PrepSchool) (optional) (default to HighSchool)
    position = 'position_example' # str | Position abbreviation filter (optional)
    state = 'state_example' # str | State or province abbreviation filter (optional)
    team = 'team_example' # str | Committed team filter (required if year not specified) (optional)

    teams = []
    try:
        # Team recruiting ratings and rankings
        api_response = api_instance.get_recruiting_teams(year=year)
    
        for data in api_response:
            team = []
            team = append_data_team(team, data)

            teams.append(team)
        return teams

    except ApiException as e:
        print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)

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