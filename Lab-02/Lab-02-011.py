# Лабораторна 2 завдання 11
import math

def calculate_expression(x, y):
    return (x + math.pi) / (x ** 2 + y ** 4 + math.e)

x = int(input("Введіть x (ціле число): "))
y = int(input("Введіть y (ціле число): "))

print(f"Результат обчислення (x + Pi)/(x^2 + y^2 + e) = {calculate_expression(x, y)}")