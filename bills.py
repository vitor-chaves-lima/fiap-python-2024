import sys

RESIDENTIAL_TYPE_ID = "r"
COMMERCIAL_TYPE_ID = "c"
INDUSTRIAL_TYPE_ID = "i"

plant_type = input("Digite o tipo do imóvel - (R)esidência, (C)omercial, (I)ndustrial: ").strip().lower()
kwh_value = float(input("Digite a quantidade em Kw/h: "))


def calc_price(min_value: float, max_value: float, kwh_limit: int, kwh_value: int):
    if kwh_value < kwh_limit:
        return kwh_value * min_value
    else:
        return kwh_value * max_value 


if(plant_type == RESIDENTIAL_TYPE_ID):
    total_value = calc_price(0.40, 0.65, 500, kwh_value)
elif(plant_type == COMMERCIAL_TYPE_ID):
    total_value = calc_price(0.55, 0.60, 1000, kwh_value)
elif(plant_type == INDUSTRIAL_TYPE_ID):
    total_value = calc_price(0.55, 0.60, 5000, kwh_value)
else:
    sys.exit("Tipo de imóvel inválido")

print(f"Valor total: R$ {total_value:.2f}")
