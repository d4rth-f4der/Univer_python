# Лабораторна 3 завдання 7

def coordinates_2d_input():
    try:
        x = int(input("Введіть координату х: "))
        y = int(input("Введіть координату y: "))
        return x, y
    except Exception:
        print("Неправильно введені дані!")
        return coordinates_2d_input()

x, y = coordinates_2d_input()
print(f"Точка А({x};{y})")