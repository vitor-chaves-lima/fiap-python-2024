PRODUCT_1_PRICE = 0.50
PRODUCT_2_PRICE = 1.00
PRODUCT_3_PRICE = 4.00
PRODUCT_4_PRICE = 7.00
PRODUCT_5_PRICE = 8.00

print("CALCULADORA PREÇOS")
print(f"1 - Produto 1 - R${PRODUCT_1_PRICE:.2f}")
print(f"2 - Produto 2 - R${PRODUCT_2_PRICE:.2f}")
print(f"3 - Produto 3 - R${PRODUCT_3_PRICE:.2f}")
print(f"4 - Produto 4 - R${PRODUCT_4_PRICE:.2f}")
print(f"5 - Produto 5 - R${PRODUCT_5_PRICE:.2f}")
print(20 * "=")

final_price = 0
while True:
    user_product_input = int(input("Digite o ID do produto: "))

    if user_product_input == 0:
        print("Finalizando conta")
        break

    user_amount_input = int(input("Digite a quantidade do produto: "))

    if user_product_input == 1:
        product_price = PRODUCT_1_PRICE * user_amount_input
    elif user_product_input == 2:
        product_price = PRODUCT_2_PRICE * user_amount_input
    elif user_product_input == 3:
        product_price = PRODUCT_3_PRICE * user_amount_input
    elif user_product_input == 4:
        product_price = PRODUCT_4_PRICE * user_amount_input
    elif user_product_input == 5:
        product_price = PRODUCT_5_PRICE * user_amount_input
    else:
        print("ID do produto inválido, nenhum valor foi adicionado")
        print(20 * "-")
        continue

    print(f"O preço adicionado é: {product_price}")
    final_price += product_price
    print(20 * "-")

print(20 * "=")
print(f"O preço final é R${final_price:.2f}")