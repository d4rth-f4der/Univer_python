# Лабораторна 2 завдання 19
import math

def calculate_radius_from_circumference(circumference):
    return circumference / (2 * math.pi)

def calculate_area_from_radius(radius):
    return math.pi * radius ** 2

circumference = float(input("Введіть довжину кола: "))
radius = calculate_radius_from_circumference(circumference)
area = calculate_area_from_radius(radius)

print(f"Радіус = {radius}, площа = {area}")