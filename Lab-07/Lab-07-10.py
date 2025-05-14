# Лабораторна 7, завдання 10
import random

def random_integers_in_range(n):
    for _ in range(n):
        yield random.randint(-10, 10)

source_list = list(random_integers_in_range(20))

sum_of_even_elements = sum(element for element in source_list if element % 2 == 0)

print(f"Вхідна послідовність: {source_list}")
print(f"Сума усіх парних елементів: {sum_of_even_elements}")