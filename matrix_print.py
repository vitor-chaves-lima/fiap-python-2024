def matrix_print(matrix: list[list[float]]):
    for r in matrix:
        c_str = [f"{c: ^5}" for c in r]
        print("[ ", end="")
        print(" ".join(c_str), end=" ")
        print("]")

if __name__ == "__main__":
    matrix_size = int(input("Digite o tamanho da matrix: "))
    matrix_val = [ [ None for _ in range(matrix_size) ] for _ in range(matrix_size) ]

    for r in range(matrix_size):
        for c in range(matrix_size):
            cell_val: float = float(input(f"Digite o valor de [{r}][{c}]: "))
            matrix_val[r][c] = cell_val

    matrix_print(matrix_val)
