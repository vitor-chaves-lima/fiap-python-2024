def char_count(text: str) -> dict[str, int]:
    char_count_dict: dict[str, int] = {}

    for char in text:
        char_count_dict[char] = 0

    for char in text:
        char_count_dict[char] += 1

    return char_count_dict

print(char_count("Os ratos"))