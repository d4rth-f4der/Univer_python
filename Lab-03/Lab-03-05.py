# Лабораторна 3 завдання 5

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

a, b, c = input_square_eq_coefficients()
print(f"Квадратне рівняння: {a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0")