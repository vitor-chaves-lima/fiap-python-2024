note_count = int(input("Digite a quantidade de notas: ").strip())
notes = []
print("=" * 30)

for i in range(note_count):
    note = float(input(f"- Digite a {i + 1}ª nota: ").strip())
    notes.append(note)

print("=" * 30)

average = 0
for (i,n) in enumerate(notes):
    print(f"{i + 1}ª Nota: {n}")
    average += n

average /= len(notes) 
print("=" * 30)
print(f"Média: {average:.2f}")