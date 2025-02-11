import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bd4371b8aeb6f3dfa7e52a89de28f611'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "Vika1998.ru@yandex.ru",
    "password": "Vika1998"
}
body_create = {
    "name": "kusik",
    "photo_id": 255
}
body_change = {
    "pokemon_id": "230022",
    "name": "pokemonik",
    "photo_id": 255
}
body_in_pokeball = {
    "pokemon_id": "230022"
}

'''response = requests.post(url = f'{URL}/trainers/reg ', headers = HEADER, json = body_registration)
print(response.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change )
print(response_change.text)

response_in_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_in_pokeball)
print(response_in_pokeball.text)
