def matrix_print(matrix: list[list[float]]):
    for r in matrix:
        c_str = [f"{c: ^5}" for c in r]
        print("[ ", end="")
        print(" ".join(c_str), end=" ")
        print("]")

def is_matrix_size_equal(a: list[list[float]], b: list[list[float]]) -> bool:
    a_rows = len(a)
    a_cols = len(a[0])

    b_rows = len(b)
    b_cols = len(b[0])

    return a_rows == b_rows and a_cols == b_cols


def sum_matrix(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    if not is_matrix_size_equal(a, b):
        raise ValueError("Matrices are not equal")

    final_matrix = [ [ None for _ in range(len(a)) ] for _ in range(len(a[0])) ]

    for r_index, r in enumerate(a):
        for c_index, _ in enumerate(r):
            final_matrix[r_index][c_index] = a[r_index][c_index] + b[r_index][c_index]

    return final_matrix

print("aaa")
matrix_print(sum_matrix([[1,2], [0,2]], [[1,5], [0,2], [0, 1]]))
