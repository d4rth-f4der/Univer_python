import re


def extract_numbers_from_file(filepath: str) -> list:
    regex = r"-?\d+\.\d+|-?\d+|\.\d+"
    numbers_found = []

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(regex, content)
            numbers_found = matches

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{filepath}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка під час обробки файлу: {e}")

    return numbers_found



file_name = "data.txt"

print(f"Шукаю числа у файлі '{file_name}'...")
extracted_numbers = extract_numbers_from_file(file_name)

if extracted_numbers:
    print("\nЗнайдені числа:")
    for number_str in extracted_numbers:
            print(number_str)
else:
    print("Чисел не знайдено.")