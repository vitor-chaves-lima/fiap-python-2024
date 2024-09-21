import requests


def get_medals_from_api(country_code: str) -> dict[str,any]:
    url = f"https://apis.codante.io/olympic-games/countries"

    r = requests.get(url)

    if r.status_code != 200:
        raise Exception("Erro ao chamar a API")

    json_data = r.json()

    country_code = country_code.upper()
    country_data = {}

    for i in json_data["data"]:
        if i["id"] == country_code:
            country_data = i
            break

    if not country_data:
        raise Exception(f"Não foi possível encontrar um país com o código {country_code}")

    country_medals = {
        "name": country_data["name"],
        "gold_medals": country_data["gold_medals"],
        "silver_medals": country_data["silver_medals"],
        "bronze_medals": country_data["bronze_medals"],
        "total": country_data["total_medals"],
        "rank": country_data["rank"],
    }

    return country_medals

country_code = input("Digite o código do pais: ")
print("-" * 50)
country_medals = get_medals_from_api(country_code)

print(f"{country_medals["name"]} ficou em {country_medals['rank']}º lugar com um total de {country_medals['total']} medalhas")
print("-" * 50)
print(f"🥇 Medalhas de ouro: {country_medals['gold_medals']}")
print(f"🥈 Medalhas de prata: {country_medals['silver_medals']}")
print(f"🥉 Medalhas de bronze: {country_medals['bronze_medals']}")