import cfbd, config
from cfbd.rest import ApiException

# Configure API key authorization: ApiKeyAuth
CONFIGURATION = cfbd.Configuration()
CONFIGURATION.api_key['Authorization'] = config.API_KEY
CONFIGURATION.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.GamesApi(cfbd.ApiClient(CONFIGURATION))

def append_data_team(team, data):
    team.append(data.team_id)
    team.append(data.year)
    team.append(data.team)
    team.append(data.conference)
    team.append(data.division)
    team.append(data.total.games)
    team.append(data.total.wins)
    team.append(data.total.losses)
    team.append(data.total.ties)
    team.append(data.conference_games.games)
    team.append(data.conference_games.wins)
    team.append(data.conference_games.losses)
    team.append(data.conference_games.ties)
    return team

def get_team_records(year):
    print(year)
    year = year # int | Recruiting class year (required if team no specified) (optional)

    teams = []
    try:
        # Team recruiting ratings and rankings
        api_response = api_instance.get_team_records(year=year)
        print(api_response)
        for data in api_response:
            team = []
            team = append_data_team(team, data)

            teams.append(team)
        return teams

    except ApiException as e:
        print("Exception when calling RecruitingApi->get_recruiting_players: %s\n" % e)
