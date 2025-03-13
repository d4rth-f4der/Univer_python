# Лабораторна 3 завдання 10

import math

def compare_cotangents(first_float, second_float):
    try:
        if 1 / math.tan(first_float) == 1 / math.tan(second_float): print(f"ctg{first_float} = ctg{second_float}")
        elif 1 / math.tan(first_float) > 1 / math.tan(second_float): print(f"ctg{first_float} > ctg{second_float}")
        else: print(f"ctg{first_float} < ctg{second_float}")
    except Exception:
        print("Неправильно введені дані")

compare_cotangents(8, 5)