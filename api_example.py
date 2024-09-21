import requests

def get_data_from_cep(cep: str) -> dict[str,any]:
    url = f"https://viacep.com.br/ws/{cep}/json"

    r = requests.get(url)

    if r.status_code != 200:
        raise Exception(r.text)

    return r.json()

cep = input("Digite o CEP: ")
print("-" * 50)
cep_data = get_data_from_cep(cep)
print(cep_data["logradouro"])
print(f"Bairro: {cep_data["bairro"]}")
print(f"Localidade: {cep_data["localidade"]}")