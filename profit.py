initial_value: float = float(input("Digite o depósito inicial: "))
mensal_value: float = float(input("Digite o depósito mensal: "))
interest_rate: float = float(input("Digite a taxa de juros mensal: "))
period_in_months: int = int(input("Digite o período: "))

current_month: int = 0
balance = initial_value
while current_month < period_in_months:
    balance= (balance + mensal_value) * (1+interest_rate)
    print(f"Mês {current_month + 1} - Saldo: {balance}")
    current_month += 1