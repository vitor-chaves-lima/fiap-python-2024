selected_grade_amount: int = int(input("Digite a quantidade de notas: "))

i = 0

grade_sum: float = 0

while i < selected_grade_amount:
    grade_value = float(input(f"Digite a nota {i + 1}: "))
    grade_sum += grade_value
    i += 1

print(selected_grade_amount)
final_grade: float = grade_sum / selected_grade_amount
print(f"A nota final é: {final_grade:.2f}")