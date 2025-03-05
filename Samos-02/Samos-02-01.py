import math


def try_variable(var):
    try:
        val = var
    except NameError:
        return None
    return val

def coordinates_2d_input():
    x = int(input("Введіть х: "))
    y = int(input("Введіть y: "))
    return x, y

def print_2d_coordinates(x,y):
    print(f"Координати точки в 2-хвимірному просторі - x = {x}, y = {y}")

def coordinates_2d():
    coordinates_exist = 0
    while True:
        action = input('ввести координати (i), вивести координати (o), назад(b): ')
        if action.lower() == 'i':
            x, y = coordinates_2d_input()
            coordinates_exist = 1
        elif coordinates_exist == 1 and action.lower() == 'o':
            print_2d_coordinates(x,y)
        elif action.lower() == 'b':
            break

def coordinates_3d_input():
    x = int(input("Введіть х: "))
    y = int(input("Введіть y: "))
    z = int(input("Введіть z: "))
    return x, y, z

def print_3d_coordinates(x,y,z):
    print(f"Координати точки в 3-хвимірному просторі - x = {x}, y = {y}, z = {z}")

def coordinates_3d():
    coordinates_exist = 0
    while True:
        action = input('ввести координати (i), вивести координати (o), назад(b): ')
        if action.lower() == 'i':
            x, y, z = coordinates_3d_input()
            coordinates_exist = 1
        elif coordinates_exist == 1 and action.lower() == 'o':
            print_3d_coordinates(x,y,z)
        elif action.lower() == 'b':
            break

def mathematical_expressions():
    a = int(input("Введіть а: "))
    b = int(input("Введіть b: "))
    formulae_1 = math.log(a ** 2 + b ** 2)
    formulae_2 = math.sin((a + b) ** (1 / 7))
    formulae_3 = (math.cos(a ** 12 + b ** 12)) ** 3
    print(f"""
    ln(a\N{SUPERSCRIPT TWO} + b\N{SUPERSCRIPT TWO}) = {formulae_1}
    sin((a + b)^1/7) = {formulae_2}
    cos\N{SUPERSCRIPT THREE}(a\N{SUPERSCRIPT ONE}\N{SUPERSCRIPT TWO} + b\N{SUPERSCRIPT ONE}\N{SUPERSCRIPT TWO}) = {formulae_3}
    """)

def triangle_perimeter():
    first_side_input = input("Введіть першу сторону трикутника: ")
    second_side_input = input("Введіть другу сторону трикутника: ")
    third_side_input = input("Введіть третю сторону трикутника: ")
    if first_side_input.isdigit() and second_side_input.isdigit() and third_side_input.isdigit():
        first_side = int(first_side_input)
        second_side = int(second_side_input)
        third_side = int(third_side_input)
        perimeter = first_side + second_side + third_side
        print(f'Периметр трикутника = {perimeter}')
    else:
        print("Некоректний ввод")

def math_module():
    while True:
        action = input("""
        Виберіть математичну функцію
        s - квадратний корінь
        log - логарифм
        sin - синус
        cos - косинус
        tan - тангенс
        fact - факторіал
        exp - піднесення е у степінь
        q - назад
        """)
        if action.lower() == 's':
            a = int(input("Введіть ціле число: "))
            print(f'\u221A{a} = {math.sqrt(a)}')
        if action.lower() == 'log':
            base = int(input("Введіть основу логарифма: "))
            a = int(input("Введіть логарифмоване число: "))
            print(f'log(base {base}){a} = {math.log(a, base)}')
        if action.lower() == 'sin':
            x = int(input("Введіть ціле число: "))
            print(f'sin({x}) = {math.sin(x)}')
        if action.lower() == 'cos':
            x = int(input("Введіть ціле число: "))
            print(f'cos({x}) = {math.cos(x)}')
        if action.lower() == 'tan':
            x = int(input("Введіть ціле число: "))
            print(f'tg({x}) = {math.tan(x)}')
        if action.lower() == 'fact':
            x = int(input("Введіть ціле число: "))
            print(f'{x}! = {math.factorial(x)}')
        if action.lower() == 'exp':
            x = int(input("Введіть ступінь експоненти: "))
            print(f'е^{x} = {math.exp(x)}')
        if action.lower() == 'q': break

def menu():
    while True:
        action = input("""
        Виберіть, що ви хочете зробити (використовуйте консоль для вводу команди):
        2d - робота з координатами точки (2D)
        3d - робота з координатами точки (3D)
        m - обчислення математичних виразів
        p - обчислення периметра трикутника
        math - використання функцій модуля math
        g - робота з геометричними об'єктами
        f - форматування чисел та виведення даних
        q - вихід: """)
        if action.lower() == '2d': coordinates_2d()
        if action.lower() == '3d': coordinates_3d()
        if action.lower() == 'm': mathematical_expressions()
        if action.lower() == 'p': triangle_perimeter()
        if action.lower() == 'math': math_module()
        if action.lower() == 'q': break


menu()