def y(x: float) -> float:
    if x <= 2:
        return x

    if x <= 3.5:
        return 2

    if x < 5:
        return 3

    return (x**2) - 10*x + 28

print(f"x = 1 -> {y(1)}")
print(f"x = 1.5 -> {y(1.5)}")
print(f"x = 2 -> {y(2)}")
print(f"x = 3.2 -> {y(3.2)}")
print(f"x = 4 -> {y(4)}")
print(f"x = 6 -> {y(6)}")
