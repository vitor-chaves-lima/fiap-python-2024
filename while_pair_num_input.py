selected_initial_number: int = int(input("Digite o número inicial: "))
selected_final_number: int = int(input("Digite o número final: "))

i = selected_initial_number
sum_range_pair_numbers = 0


while i < selected_final_number:
    if(i % 2 == 0):
        sum_range_pair_numbers += i
    
    i += 1

print(f"Soma de todos os números pares no intervalo selecionado: {sum_range_pair_numbers}")