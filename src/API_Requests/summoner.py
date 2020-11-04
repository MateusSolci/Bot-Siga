import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import *
load_dotenv()


# retorna informações do invocador, a partir do nickname
def summoner_ids(origin, nick):
    response = Request().makeRequest(origin + "/lol/summoner/v4/summoners/by-name/" + nick + "?api_key=" + os.environ.get('key'))

    return response


def get_elo(origin, id):
    response = Request().makeRequest(origin + "/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def mastery(origin, id):
    response = Request().makeRequest(origin + "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def live_game(origin, id):
    response = Request().makeRequest(origin + "/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def summoner_info(self, origin, nick):
    IDs = summoner_ids(origin, nick)
    elo = get_elo(origin, IDs['id'])
    mastery = mastery(origin, IDs['id'])

    summonerJson = {}

    return summonerJson
