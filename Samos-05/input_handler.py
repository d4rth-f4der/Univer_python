import math

def get_input():

    while True:
        try:
            rad = float(input("Введіть значення кута в радіанах: "))
            eps = float(input("Введіть бажану точність (наприклад, 1e-6): "))
            if eps <= 0:
                print("Точність має бути додатньою.")
                continue
            effective_rad = rad % (2 * math.pi)
            return effective_rad, eps
        except ValueError:
            print("Будь ласка, введіть дійсні числа.")

def get_input_with_predefined(rad, eps):
    effective_rad = rad % (2 * math.pi)
    return effective_rad, eps