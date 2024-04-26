MULTIPLE_LIMIT: int = 10

number: int = int(input("Digite o número: "))

iterator: int = 1
while iterator <= 10:
    multiple_result = number * iterator
    print(f"{number} * {iterator} = {multiple_result}")
    iterator += 1