# Лабораторна робота 5 завдання 1
# Початковий код
def f(n):
    if n <=0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)

# Ітеративна функція
def get_fibonacci_value_of_index(n):
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        next = a + b
        a = b
        b = next
    return b

import time

start_time = time.process_time()
print(get_fibonacci_value_of_index(36))
end_time = time.process_time()
print(f"ітеративний час для 36 елемента Фібоначчі: {end_time - start_time:.10f}")

start_time = time.process_time()
print(f(36))
end_time = time.process_time()
print(f"рекурсивний час для 36 елемента Фібоначчі: {end_time - start_time:.10f}")