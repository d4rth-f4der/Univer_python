# Лабораторна 2 завдання 10
import math

def calculate_expression(x, y, z):
    return math.exp(x) + 2 * y * z

x = int(input("Введіть x (ціле число): "))
y = int(input("Введіть y (ціле число): "))
z = int(input("Введіть z (ціле число): "))

print(f"Результат обчислення е^x + 2yz = {calculate_expression(x, y, z)}")