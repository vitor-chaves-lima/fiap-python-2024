# 1
fruits: dict[str, str] = {
    "laranja": "laranja",
    "abacate": "verde",
    "morango": "vermelho"
}

# 2
print(fruits["morango"])

# 3
fruits["abacaxi"] = "amarelo"
print(fruits)

# 4
fruits["laranja"] = "roxo"
print(fruits)

# 5
del fruits["abacaxi"]
print(fruits)

# 6
for f in fruits.keys():
    print(f)

# 7
for f in fruits.values():
    print(f)

# 8
if "banana" not in fruits:
    print("Banana não está na lista")

# 9
new_fruits: dict[str, str] = {
    "uva": "roxo"
}

fruits.update(new_fruits)
print(fruits)

# 10
print(f"Quantidade de frutas no dict: {len(fruits)}")