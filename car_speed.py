CHARGE_VALUE: float = 5
MAX_SPEED: int = 80

speed: int = int(input("Digite a velocidade do carro: "))

if speed > MAX_SPEED:
    overspeed: int = speed - MAX_SPEED
    charge: float = CHARGE_VALUE * overspeed

    print(f"O motorista estava à {speed} KM/h, com uma overspeed de {overspeed} KM/h. A multa é de R$ {charge}")

if speed <= 80:
    print("Multo bem! Você está dentro do limite")