row_count: int = int(input("Digite o número de linhas: "))
max_content_width: int = 2*row_count - 1

for i in range(0,row_count):
    row_content = "*"*((i*2) +1)
    print(f"{row_content:^{max_content_width}}")
