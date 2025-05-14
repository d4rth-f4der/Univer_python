# Лабораторна 7, завдання 9
import random

def random_integers_in_range(n):
    for _ in range(n):
        yield random.randint(-10, 10)

source_list = list(random_integers_in_range(20))

smallest_positive = min((element for element in source_list if element > 0), default=None)

print(f"Вхідна послідовність: {source_list}")
print(f"Найменший додатній елемент: {smallest_positive}")