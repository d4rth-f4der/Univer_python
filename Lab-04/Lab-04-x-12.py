# Lab 04 task `12
import math

def calculate_square_roots_expression(n: int):
    expression = math.sqrt(3 * n)
    for i in range (n-1, 0, -1):
        expression = math.sqrt((3 * i) + expression)
    return expression

print(calculate_square_roots_expression(1))
print(math.sqrt(3))     # перевірка
print(calculate_square_roots_expression(2))
print(math.sqrt(3 + math.sqrt(3*2)))    # перевірка
print(calculate_square_roots_expression(3))
print(math.sqrt(3 + math.sqrt(3*2 + math.sqrt(3*3))))   # перевірка