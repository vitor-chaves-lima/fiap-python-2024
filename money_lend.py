customer_age: int = int(input("Digite a idade do cliente: "))
customer_salary: float = float(input("Digite o salário do cliente: "))
flag: bool = False

minimum_age: int = 18
minimum_salary: float = 1500.00

can_lend: bool = (customer_age >= minimum_age and customer_salary >= minimum_salary) or flag
print(f"O cliente pode fazer o empréstimo? {can_lend}")