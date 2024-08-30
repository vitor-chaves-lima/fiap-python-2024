def matrix_print(matrix: list[list[float]]):
    for r in matrix:
        c_str = [f"{c: ^5}" for c in r]
        print("[ ", end="")
        print(" ".join(c_str), end=" ")
        print("]")

test_matrix = [
    [0, 1, 5],
    [1, 3, 4],
    [5000, 10000, -2000]
]
print("PRINT")
matrix_print(test_matrix)
