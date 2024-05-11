def list_sum(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])

    return new_list

a = [0, 2, 3]
b = [0, 3, 4]
c = list_sum(a, b)
print(c)