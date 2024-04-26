user_number_input: int = int(input("Digite um valor: "))
print("=" * 20)

iterator: int = 1
final_sum: int = 0
while iterator <= user_number_input:
    value_before_sum = final_sum
    final_sum += iterator
    print(f"{value_before_sum} + {iterator} = {final_sum}")
    iterator += 1

print("=" * 20)
print(f"Resultado final: {final_sum}")