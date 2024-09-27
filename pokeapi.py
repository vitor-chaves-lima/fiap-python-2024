from requests import request

API_URL = "https://pokeapi.co/api/v2/pokemon"

pokemon_name = input("Digite o nome de um pokémon: ").lower()
request_url = f"{API_URL}/{pokemon_name}"

r = request("GET", request_url)

if r.status_code != 200:
    raise Exception("Aconteceu um erro durante a requisição para a API", r.text)

response_data = r.json()
pokemon_id = response_data["id"]
pokemon_types = response_data["types"]

print("=" * 50)
print(f"O ID do Pokémon é: {pokemon_id}")
print("TIPOS: ")
for t in pokemon_types:
    print(f"* {t["slot"]} - {t["type"]["name"]}")