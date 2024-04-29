user_input_value: int = int(input("Digite a quantidade de termos da sequência: "))

last_term: int = 0
current_term: int = 1

if user_input_value == 0 or user_input_value == 1:
    print(last_term)
    print(current_term)
else :    

    iterator: int = 0
    while iterator < user_input_value:
        next_term = last_term + current_term
        last_term = current_term
        current_term  = next_term
        print(current_term)
        iterator += 1