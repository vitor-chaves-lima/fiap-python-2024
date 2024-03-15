salary: float = float(input("Digite o salário: "))

raise_value: float = salary * 0.15
new_salary: float = salary + raise_value

print(f"O valor do aumento foi de: {raise_value}")
print(f"O novo salário é: {new_salary}")