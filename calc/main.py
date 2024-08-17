import oper1
import oper2

o = input("digite +,-,*,/ para a operação desejada: ")
val = []
while True:
    num = input("Digite o valor ou s para sair: ")

    if num != 's':
        val.append(float(num))
    else:
        break

if o == "+":
    res = oper1.sum(*val)
elif o == "-":
    res = oper1.sub(*val)
elif o == "*":
    res = oper2.mult(*val)
elif o == "/":
    res = oper2.div(*val)
else:
    exit("Operação inválida")

print(f"O resultado da {o} é: {res}")
