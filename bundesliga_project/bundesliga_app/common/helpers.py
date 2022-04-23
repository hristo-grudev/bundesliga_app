from suds.client import Client
from datetime import datetime as dt
from datetime import time
import requests

LEAGUE_SAISON = "2021"
URL = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"
client = Client(URL)


def get_current_group(name):
    return client.service.GetCurrentGroup(name).groupOrderID


def get_upcoming_matches(name, date):
    from_date_time = dt.combine(date, time(0, 0, 0))
    to_date_time = dt.combine(date, time(23, 59, 59))
    print(from_date_time, to_date_time)
    return client.service.GetMatchdataByLeagueDateTime(from_date_time, to_date_time, name).Matchdata


def get_all_matches(name):
    return client.service.GetMatchdataByLeagueSaison(name, LEAGUE_SAISON).Matchdata


def get_all_teams(name):
    url = f'https://api.openligadb.de/getbltable/{name}/{LEAGUE_SAISON}'
    response = requests.get(url)
    print(response.json()[0])
    return response.json()
