a = "Bom dia!"

# len retorna o tamanho da string
len(a) 

# Um índice negativo de string serve para acessar a string de trás pra frente
print(a[-1])

# Os : servem para fatiar (criar um slice) a string ( exclusive no fim )
# É possível retirar um dos valores antes ou depois dos :
print(a[2:5])
print(a[2:])
print(a[:5])
print(a[:-2])
print(a[-5:-2])
