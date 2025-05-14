# Лабораторна 7, завдання 20
my_list = [5, 2, 8, 3, 1, 6, 10, 7, 4, 9]
print(f"Початковий список: {my_list}")

# Сортуємо список my_list за правилом: парні (за зростанням), потім непарні (за зростанням).
my_list.sort(key=lambda x: (x % 2 != 0, x))
print(f"Відсортований список: {my_list}")

another_list = [-3, 0, 11, -4, 7, 2]
print(f"\nПочатковий список: {another_list}")

another_list.sort(key=lambda x: (x % 2 != 0, x))
print(f"Відсортований список: {another_list}")