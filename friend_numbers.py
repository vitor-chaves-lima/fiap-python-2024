def get_division_sum(value):
    division_sum = 0
    for i in range(1, value):
        if value % i == 0:
            division_sum += i

    return division_sum

a = 220
b = 284

def friends(a, b):
    return get_division_sum(b) ==  a and get_division_sum(a) == b

print(friends(a, b))