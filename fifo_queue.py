queue = []

while True:
    command = input("Digite A para adicionar na fila ou R para remover da fila: ").lower().strip()
    print("=" * 30)

    if command == "a":
        username = input("Digite o nome da pessoa: ")
        queue.append(username)
        print(f"{username} adicionado")
    elif command == "r":
        removed_user = queue.pop(0)
        print(f"{removed_user} foi atendido!")

    print(f"Fila: {queue} - Tamanho: {len(queue)}")

    print("=" * 30)

    exit_program = input("Deseja encerrar a fila? (S para encerrar): ").lower().strip()
    if exit_program == "s":
       break