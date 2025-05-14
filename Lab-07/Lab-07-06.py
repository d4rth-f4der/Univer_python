# Лабораторна 7, завдання 6
import random

def random_integers_in_range(n):
    for _ in range(n):
        yield random.randint(-1000, 1000)

source_seq = list(random_integers_in_range(20))

print("Послідовність:", source_seq)
count = sum(1 for element in source_seq if element > 0)
print(f"\nКількість додатних елементів у послідовності (вираз): {count}")