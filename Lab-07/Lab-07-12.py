# Лабораторна 7, завдання 12
import random

def random_integers_in_range(n):
    for _ in range(n):
        yield random.randint(-10, 10)

source_list = list(random_integers_in_range(20))

sum_of_even_indexed_elements = sum(element for index, element in enumerate(source_list) if index % 2 == 0)

sum_of_odd_indexed_elements = sum(element for index, element in enumerate(source_list) if index % 2 != 0)

print(f"Вхідна послідовність: {source_list}")
print(f"Сума елементів з парними індексами: {sum_of_even_indexed_elements}")
print(f"Сума елементів з непарними індексами: {sum_of_odd_indexed_elements}")