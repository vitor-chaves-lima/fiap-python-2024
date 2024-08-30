# x_value: float = float(input("Digite o valor de x: "))


def y(x_value: float) -> float:
    y_value: float = 0

    if x_value < 0:
        y_value = x_value ** 2
    elif x_value >= 0 and x_value < 5:
        y_value = x_value
    else:
        y_value = 6

    return y_value

print(f"x = 0 -> {y(0)}")
print(f"x = -5 -> {y(-5)}")
print(f"x = 5 -> {y(5)}")
print(f"x = 10 -> {y(10)}")