selected_number: int = int(input("Digite um número limite: "))

i = 0
while i < selected_number:
    i += 1

    if(i % 2 == 0):
        print(i)