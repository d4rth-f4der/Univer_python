# Лабораторна 7, завдання 11

# вираз-генератор, що задає підпослідовність
import random

def mixed_types_generator(n):
    for _ in range(n):
        yield random.randint(-10, 10)                                          # Ціле число (int)
        yield random.randint(-10, 10) + 0.5                                    # Дійсне число (float)
        yield f"text_{random.randint(-10, 10)}"                                # Рядок (str)
        yield None                                                                # Тип NoneType

source_list = list(mixed_types_generator(10))

sum_of_numerical_elements = sum(element for element in source_list if isinstance(element, (int, float)))

print(f"Вхідна послідовність (перші 16 елементів): {source_list}")
print(f"Кількість елементів у послідовності: {len(source_list)}")
print(f"\nСума усіх числових елементів: {sum_of_numerical_elements}")