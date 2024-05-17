def calc_delta(a,b,c):
    delta_value: float = b**2 - (4 * a * c)
    return delta_value

def calc_roots(a, b, delta) -> tuple[float, int]:
    x1 = (-b + (delta ** (1/2)))/(2 * a)
    x2 = (-b - (delta ** (1/2)))/(2 * a)

    return (x1, x2)


a = 1
b = 5
c = 6
delta = calc_delta(a,b,c)
print(f"O delta é: {delta}")

(x1, x2) = calc_roots(a,b,delta)
print(f"X1: {x1}, X2: {x2}")