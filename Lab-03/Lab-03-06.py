# Лабораторна 3 завдання 6

def input_line_eq_coefficients():
    try:
        a = int(input("Введіть коефіцієнт а рівняння прямої: "))
        b = int(input("Введіть коефіцієнт b рівняння прямої: "))
        if a == 0 == b:
            print("Коефіцієнти а і b не можуть одночасно дорівнювати 0!")
            return input_line_eq_coefficients()
        c = int(input("Введіть коефіцієнт c рівняння прямої: "))
        return a, b, c
    except Exception:
        print("Неправильний ввод!")
        return input_line_eq_coefficients()

a, b, c = input_line_eq_coefficients()
print(f"Рівняння прямої: {a}x + {b}y + {c} = 0")