num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))

command = int(input("Digite a operação: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão"))

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

if command == 1:
    result = sum(num1, num2)
    print(f"Resultado da soma: {result}")
elif command == 2:
    result = sub(num1, num2)
    print(f"Resultado da subtração: {result}")
elif command == 3:
    result = mul(num1, num2)
    print(f"Resultado da multiplicação: {result}")
elif command == 4:
    result = div(num1, num2)
    print(f"Resultado da divisão: {result}")
else:
    print("Operação inválida, saindo do programa")
    exit(-1)