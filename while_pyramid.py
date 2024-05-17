max_number: int = int(input("Digite um número: "))

current_output = ""
current_number = 1
while current_number <= max_number:
    current_output += str(current_number) + " "
    print(current_output)
    current_number += 1
