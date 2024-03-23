days: int = int(input("Digite a quantidade de dias: "))
hours: int = int(input("Digite a quantidade de horas: "))
minutes: int = int(input("Digite a quantidade de minutos: "))
seconds: int = int(input("Digite a quantidade de segundos: "))

days_to_sec: int = days * 24 * 60 * 60
hours_to_sec: int = hours * 60 * 60
minutes_to_sec: int = minutes * 60

total: int = days_to_sec + hours_to_sec + minutes_to_sec + seconds
print(f"Total de segundos: {total}")