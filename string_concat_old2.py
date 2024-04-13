name = "Maria"
age = 25
salary = 4650.37

msg = '%s tem %d anos e ganha R$%.2f' % (name, age, salary)
print(msg)

msg2 = "[{:-^20s}] tem {} anos e ganha R${:.2f}".format(name, age, salary)
print(msg2)

msg3 = f"[{name:-^20s}] tem {age} anos e ganha R${salary:.2f}"
