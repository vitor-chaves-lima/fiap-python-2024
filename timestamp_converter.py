#timestamp: int = int(input("Digite o timestamp: "))
timestamp: int = 87426

hours = timestamp // 3600
hour_remaining = timestamp % 3600 

minutes = hour_remaining // 60
minutes_remaining = hour_remaining % 60
seconds = minutes_remaining

print(f"{hours}:{minutes}:{seconds}")





### VAI CAIR SÉCULOS NO CP