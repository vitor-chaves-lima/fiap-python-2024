nota1: float = float(input("- Digite a nota 1: "))
nota2: float = float(input("- Digite a nota 2: "))
nota3: float = float(input("- Digite a nota 3: "))

average: float = (nota1 + nota2 + nota3) / 3
print(f"Média: {average}")

approved = False

if average >= 6:
    approved = True

print(f"Aluno aprovado? {approved}")