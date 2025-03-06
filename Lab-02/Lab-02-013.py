# Лабораторна 2 завдання 13
def coordinates_3d_input():
    x = int(input("Введіть х: "))
    y = int(input("Введіть y: "))
    z = int(input("Введіть z: "))
    return x, y, z

def print_3d_coordinates(x, y, z):
    print(f"Координати точки в 3-хвимірному просторі - x = {x}, y = {y}, z = {z}, A({x};{y},{z})")

print("Для точки А у просторі введіть координати")
x, y, z = coordinates_3d_input()
print_3d_coordinates(x, y, z)