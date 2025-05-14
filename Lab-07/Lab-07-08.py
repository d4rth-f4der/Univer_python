# Лабораторна 7, завдання 8
import random

def random_integers_in_range(n):
    for _ in range(n):
        yield random.randint(-10, 10)

source_seq = list(random_integers_in_range(20))

element_to_find = 5

positions_list = [index for index, element in enumerate(source_seq) if element == element_to_find]

print(f"Вхідна послідовність: {source_seq}")
print(f"Елемент для пошуку (el): {element_to_find}")
print(f"Послідовність позицій, де знайдено {element_to_find}: {positions_list}")