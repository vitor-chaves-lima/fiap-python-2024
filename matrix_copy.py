a = [[1,2,3], [4,5,6], [7,8,9]]
b = [i[:] for i in a]

print(a)
print(b)

a[0][0] = 7

print(a)
print(b)