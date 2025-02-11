import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bd4371b8aeb6f3dfa7e52a89de28f611'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '18094'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'kusik'

@pytest.mark.parametrize('key, value', [('name', 'kusik'), ('trainer_id', TRAINER_ID), ('id', '230022')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value