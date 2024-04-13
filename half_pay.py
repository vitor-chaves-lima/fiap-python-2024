age = int(input("Digite sua idade: "))
student_string = int(input("Você possuí carteira de estudante? 1 - Sim | 0 - Não: "))
student = student_string == 1

half_pay = False

if (age <= 21 or age >= 65) or student == True:
    half_pay = True

print("Você paga meia entrada?", half_pay)