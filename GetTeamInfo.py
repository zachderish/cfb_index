import cfbd, config
from cfbd.rest import ApiException

# Configure API key authorization: ApiKeyAuth
CONFIGURATION = cfbd.Configuration()
CONFIGURATION.api_key['Authorization'] = config.API_KEY
CONFIGURATION.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(CONFIGURATION))

def append_data_team(team, data):
    team.append(data.team)
    team.append(data.team)
    team.append(data.points)
    return team

def get_team_records(year, conference):
    print(year)
    year = year # int | Recruiting class year (required if team no specified) (optional)
    conference = conference

    teams = []
    try:
        # Team recruiting ratings and rankings
        api_response = api_instance.get_team_records(year=year, conference=conference)
        print(api_response)
        return
        for data in api_response:
            team = []
            team = append_data_team(team, data)

            teams.append(team)
        return teams

    except ApiException as e:
        print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)