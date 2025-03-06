# Лабораторна 2 завдання 12
import math

def input_coordinates():
    x1 = int(input("Введіть першу координату точки: "))
    x2 = int(input("Введіть другу координату точки: "))
    return x1, x2

def triangle_perimeter(x1, x2, y1, y2, z1, z2):
    ab = math.sqrt((y1 - x1) ** 2 + (y2 - x2) ** 2)
    ac = math.sqrt((z1 - x1) ** 2 + (z2 - x2) ** 2)
    bc = math.sqrt((z1 - y1) ** 2 + (z2 - y2) ** 2)
    return ab + ac + bc

print("для першої точки трикутника")
x1, x2 = input_coordinates()
print("для другої точки трикутника")
y1, y2 = input_coordinates()
print("для третьої точки трикутника")
z1, z2 = input_coordinates()

print(f'Периметр трикутника = {triangle_perimeter(x1, x2, y1, y2, z1, z2)}')