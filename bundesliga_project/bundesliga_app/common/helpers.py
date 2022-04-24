from suds.client import Client
from datetime import datetime as dt
from datetime import time
import requests

URL = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"
client = Client(URL)


def last_league_season():
    leagues = client.service.GetAvailLeagues().League
    last_season = [league.leagueSaison for league in leagues if league.leagueShortcut in ['bl1', 'bl2', 'bl3']]
    return max(last_season)


LEAGUE_SAISON = last_league_season()


def get_current_group(name):
    return client.service.GetCurrentGroup(name).groupOrderID


def get_upcoming_matches(name, date):
    from_date_time = dt.combine(date, time(0, 0, 0))
    to_date_time = dt.combine(date, time(23, 59, 59))
    try:
        data = client.service.GetMatchdataByLeagueDateTime(from_date_time, to_date_time, name)
    except Exception as e:
        data = []
    return data


def get_all_matches(name):
    try:
        data = client.service.GetMatchdataByLeagueSaison(name, LEAGUE_SAISON).Matchdata
    except Exception as e:
        data = []
    return data

def get_all_teams(name):
    url = f'https://api.openligadb.de/getbltable/{name}/{LEAGUE_SAISON}'
    response = requests.get(url)
    return response.json()
