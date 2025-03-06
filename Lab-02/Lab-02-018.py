# Лабораторна 2 завдання 18
import math

def calculate_function(a, x):
    f_a_x = math.fabs(x ** 5 + math.fabs ( a * x - x ** 3) - a) + a * x ** 2 + a ** 8
    return f_a_x

print("Обчислення значення функції f(a,x) = |x\N{SUPERSCRIPT FIVE} + |ax - x\N{SUPERSCRIPT THREE}| - a| + ax\N{SUPERSCRIPT TWO} + a\N{SUPERSCRIPT EIGHT}")
a = float(input("Введіть значення аргументу а: "))
x = float(input("Введіть значення аргументу х: "))

print(f"Для а = {a}, x = {x}: f(x,a) = {calculate_function(a, x)}")