import math

def input_number_with_check():
    input_string = input("Введіть число: ")
    try:
        input_float = float(input_string)
        if input_float == 0: return int(input_float)
        elif input_float.is_integer(): return int(input_float)
        else: return input_float
    except ValueError:
        print("неправильні дані!")
        return input_number_with_check()

def input_positive_number_with_check():
    input_string = input("Введіть число: ")
    try:
        input_float = float(input_string)
        if input_float > 0:
            if input_float.is_integer():
                return int(input_float)
            else:
                return input_float
        else:
            print("Число має бути більше 0!")
            return input_positive_number_with_check()
    except ValueError:
        print("неправильні дані!")
        return input_positive_number_with_check()

def coordinates_2d_input():
    print("Ввод х")
    x = input_number_with_check()
    print("Ввод y")
    y = input_number_with_check()
    return x, y

def print_2d_coordinates(x,y):
    if x == 0: x = int(x);
    elif x % int(x) == 0: x = int(x)
    if y == 0: y = int(y);
    elif y % int(y) == 0: y = int(y)
    print(f"Координати точки в 2-хвимірному просторі - x = {x}, y = {y},"
          f"\nінший вигляд: А({x};{y})")

def coordinates_2d():
    coordinates_exist = 0
    while True:
        action = input('ввести координати (i), вивести координати (o), назад(b): ')
        if action.lower() == 'i':
            x, y = coordinates_2d_input()
            coordinates_exist = 1
        if coordinates_exist == 1 and action.lower() == 'o':
            print_2d_coordinates(x,y)
        if action.lower() == 'b':
            break

def coordinates_3d_input():
    print("Ввод х")
    x = input_number_with_check()
    print("Ввод y")
    y = input_number_with_check()
    print("Ввод z")
    z = input_number_with_check()
    return x, y, z

def print_3d_coordinates(x,y,z):
    if x == 0: x = int(x);
    elif x % int(x) == 0: x = int(x)
    if y == 0: y = int(y);
    elif y % int(y) == 0: y = int(y)
    if z == 0: z = int(z);
    if z % int(z) == 0: z = int(z)
    print(f"Координати точки в 3-хвимірному просторі - x = {x}, y = {y}, z = {z},"
          f"\nінший вигляд: А({x};{y};{z})")

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
    print("Ввод а")
    a = input_number_with_check()
    print("Ввод b")
    b = input_number_with_check()
    formulae_1 = math.log(a ** 2 + b ** 2)
    formulae_2 = math.sin((a + b) ** (1 / 7))
    formulae_3 = (math.cos(a ** 12 + b ** 12)) ** 3
    print(f"""
    ln(a\N{SUPERSCRIPT TWO} + b\N{SUPERSCRIPT TWO}) = {formulae_1}
    sin((a + b)^1/7) = {formulae_2}
    cos\N{SUPERSCRIPT THREE}(a\N{SUPERSCRIPT ONE}\N{SUPERSCRIPT TWO} + b\N{SUPERSCRIPT ONE}\N{SUPERSCRIPT TWO}) = {formulae_3}
    """)

def triangle_perimeter():
    print("Перша сторона трикутника")
    side1 = input_positive_number_with_check()
    print("Друга сторона трикутника")
    side2 = input_positive_number_with_check()
    print("Третя сторона трикутника")
    side3 = input_positive_number_with_check()
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        perimeter = side1 + side2 + side3
        print(f'Периметр трикутника = {perimeter}')
    else:
        print("Такого трикутника не існує, перевірте правильність даних")

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
        q - назад: """)

        if action.lower() == 's':
            a = input_positive_number_with_check()
            print(f'\u221A{a} = {math.sqrt(a)}')

        if action.lower() == 'log':
            print("Основа логарифма")
            base = input_positive_number_with_check()
            if base == 1:
                print("Основа на може бути 1!")
                base = input_positive_number_with_check()
            print("Аргумент логарифма")
            a = input_positive_number_with_check()
            res = math.log(a, base)
            if res == 0: res = int(res)
            print(f'log(base {base}){a} = {res}')

        if action.lower() == 'sin':
            print("кут (радіани)")
            x = input_number_with_check()
            print(f'sin({x}) = {math.sin(x)}')

        if action.lower() == 'cos':
            print("кут (радіани)")
            x = input_number_with_check()
            print(f'cos({x}) = {math.cos(x)}')

        if action.lower() == 'tan':
            print("кут (радіани)")
            x = input_number_with_check()
            print(f'tg({x}) = {math.tan(x)}')

        if action.lower() == 'fact':
            x = input_positive_number_with_check()
            if x.is_integer(): print(f'{x}! = {math.factorial(x)}')
            else:
                print("Число має бути цілим!")

        if action.lower() == 'exp':
            print("ступінь експоненти")
            x = input_number_with_check()
            res = math.exp(x)
            if res == 1: res = int(res)
            print(f'е^{x} = {res}')

        if action.lower() == 'q': break

def calculate_radius_from_circumference(circumference):
    return circumference / (2 * math.pi)

def calculate_area_from_radius(radius):
    return math.pi * radius ** 2

def circle_module():
    while True:
        action = input("""
        Виберіть геометричну функцію:
        r - обчислення радіуса за довжиною кола
        a - обчислення площі круга за радіусом
        ra - обчислення радіуса і площі за довжиною кола
        q - вихід: """)

        if action.lower() == 'r':
            print("Довжина кола")
            circumference = input_positive_number_with_check()
            print(f"радіус = {calculate_radius_from_circumference(circumference)}")

        if action.lower() == 'a':
            print("радіус")
            radius = input_positive_number_with_check()
            print(f"площа круга = {calculate_area_from_radius(radius)}")

        if action.lower() == 'ra':
            print("Довжина кола")
            circumference = input_positive_number_with_check()
            radius = calculate_radius_from_circumference(circumference)
            area = calculate_area_from_radius(radius)
            print(f"радіус = {radius}, площа = {area}")

        if action.lower() == 'q': break

def format_module():
    number = input_number_with_check()
    number_dot_digits = int(input("введіть кількість знаків після коми: "))
    res_rounded = round(number, number_dot_digits)
    print(f'число = {res_rounded}')
    print(f'scientific = {number:.2e}')

def print_equation(a, b):
    print(f'Рівняння: {a}x + {b} = 0')

def equation_interface():
    print("аргумент а")
    a = input_number_with_check()
    print("аргумент b")
    b = input_number_with_check()
    print_equation(a, b)

def greetings():
    name = input("Введіть ваше ім'я: ")
    surname = input("Введіть ваше прізвище: ")
    print(f'Привіт, {name} {surname}!')

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
        eq - рівняння
        greet - привітання
        q - вихід: """)
        if action.lower() == '2d': coordinates_2d()
        if action.lower() == '3d': coordinates_3d()
        if action.lower() == 'm': mathematical_expressions()
        if action.lower() == 'p': triangle_perimeter()
        if action.lower() == 'math': math_module()
        if action.lower() == 'g': circle_module()
        if action.lower() == 'f': format_module()
        if action.lower() == 'eq': equation_interface()
        if action.lower() == 'greet': greetings()
        if action.lower() == 'q': break

menu()