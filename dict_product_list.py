buy_list: [str] = ["biscoito", "chocolate", "farinha"]
total_price: float = 0.0

products_list: dict[str, float] = {
    "amaciante":4.99,
    "arroz":10.90,
    "biscoito":1.69,
    "cafe":6.98,
    "chocolate":3.79,
    "farinha":2.99
}

for i in buy_list:
    product_price = products_list.get(i)

    if product_price is None:
        print(f"{i} não existe na lista do supermercado")
    else:
        print(f"{i} - R$ {product_price}")
        total_price += product_price


print("=" * 50)
print(f"Total: {total_price:.2f}")
