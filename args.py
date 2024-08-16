def sum_with_args(*args) -> int:
    final_sum = 0
    for v in args:
        final_sum += v

    return final_sum

param_count = int(input("Digite a quantidade de parâmetros que você desja somar: "))
params = []


for i, v in enumerate(range(param_count)):
    param_value = float(input(f"Digite o valor nº {i+1}: "))
    params.append(param_value)

sum_result = sum_with_args(*params)
print(f"O resultado da soma é: {sum_result}")
