# Лабораторна 7, завдання 7

input_string = "Це рядок з цифрами 123 та 45."
count_of_digits = sum(1 for char in input_string if char.isdigit())


print(f"Вхідний рядок: \"{input_string}\"")
print(f"Кількість входжень десяткових цифр у рядку: {count_of_digits}")