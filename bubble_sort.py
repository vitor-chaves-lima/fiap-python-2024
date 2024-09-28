list_values = [153,214,569,20,102,111,3,112,623,186,300,882]

def switch_values(list_: list[int], i: int, j: int) -> list[int]:
    m = list_[i]
    list_[i] = list_[j]
    list_[j] = m
    return list_


for iteration in range(len(list_values) - 1, 0, -1):
    for index, value in enumerate(list_values[:iteration]):
        if value > list_values[index + 1]:
            list_values = switch_values(list_values, index, index+1)

    if iteration == 1:
        break

print(list_values)