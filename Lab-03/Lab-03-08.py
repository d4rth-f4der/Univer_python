# Лабораторна 3 завдання 8
import math

def input_square_eq_coefficients():
    try:
        a = int(input("Введіть коефіцієнт а квадратного рівняння: "))
        if a == 0:
            print("Коефіцієнт а не може дорівнювати 0!")
            return input_square_eq_coefficients()
        b = int(input("Введіть коефіцієнт b квадратного рівняння: "))
        c = int(input("Введіть коефіцієнт c квадратного рівняння: "))
        return a, b, c
    except Exception:
        print("Неправильний ввод!")
        return input_square_eq_coefficients()

def print_square_eq_from_coefficients(a, b, c):
    print(f"Квадратне рівняння: {a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0")

def print_res_square_eq_from_coefficients(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr < 0: print(f"D = {discr}, Система не має розв'язків.")
    elif discr == 0: print(f"D = {discr}, система має 1 розв'язок, х = ", -b / (2 * a))
    else: print(f"D = {discr}, система має 2 розв'язки, х1 = {(-b + math.sqrt(discr)) / (2 * a)};"
                f"x2 = {(-b - math.sqrt(discr)) / (2 * a)}")

def calc_square_eq():
    a, b, c = input_square_eq_coefficients()
    print_square_eq_from_coefficients(a, b, c)
    print_res_square_eq_from_coefficients(a, b, c)

calc_square_eq()