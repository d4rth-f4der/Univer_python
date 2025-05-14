# Лабораторна 7, завдання 16
import random

def infinite_random_integers(n):
    for _ in range(n):
        yield random.randint(-10, 10)

current_sequence = list(infinite_random_integers(random.randint(0, 20)))

sequence_length = sum(1 for _ in current_sequence)

print(f"Вхідна послідовність: {current_sequence}")
print(f"Довжина послідовності (обчислено виразом sum): {sequence_length}")