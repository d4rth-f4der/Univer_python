# Лабораторна 3 завдання 11
import math


def calc_triangle_area_from_sides(side1, side2, side3):
    try:
        if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
            half_p = (side1 + side2 + side3) / 2
            area = math.sqrt(half_p * (half_p - side1) * (half_p - side2) * (half_p - side3))
            return area
        else:
            print("Такого трикутника не існує, перевірте правильність даних")
    except Exception:
        print("Неправильно введені дані")

area = calc_triangle_area_from_sides(7,8,12)
if area: print(f"Площа трикутника = {area}")