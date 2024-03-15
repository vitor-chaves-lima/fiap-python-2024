a: float = float(input("Digite o valor de A: "))
b: float = float(input ("Digite o valor de B: "))
c: float = float(input("Digite o valor de C: "))

print(f"- Equação delta: ({b} ** 2) - (4 * {a} * {c})")
delta: float = (b ** 2) - 4 * a * c
print(f"- Delta: {delta}")

print(f"- Equação X1 : (-{b}) + ({delta} ** 1/2) / 2 * {a}")
print(f"- Equação X2 : (-{b}) - ({delta} ** 1/2) / 2 * {a}")

x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

print(f"X1: {x1}")
print(f"X2: {x2}")