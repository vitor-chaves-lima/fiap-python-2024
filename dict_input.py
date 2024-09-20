from datetime import datetime

people_count: int = int(input("Digite a quantidade de pessoas: "))
print("=" * 50)

people: dict[str, str] = {}

for i in range(people_count):
    person_index = (i + 1)
    person_name: str = input("Digite o nome da pessoa %d: " % person_index)
    person_age: int = datetime.now().year - int(input("Digite o ano de nascimento da pessoa: "))
    person_gender: str = input("Digite o gênero da pessoa %d: " % person_index)
    people[person_name] = {'age': person_age, 'gender': person_gender}

    print("=" * 50)

print(people)