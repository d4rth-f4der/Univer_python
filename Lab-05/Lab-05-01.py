# Лабораторна робота 5 завдання 1
"""
Початковий код:

x = float(input('Input a float from [0;1]: '))
if x < 0 or x > 1:
    raise ValueError('Your number not in [0;1]')
"""

floor_number = 0
ceiling_number = 1
x = float(input(f'Input a float number from {floor_number} to {ceiling_number}: '))
if not (floor_number <= x <= ceiling_number):
    raise ValueError(f"This number doesn't belong to [{floor_number};{ceiling_number}]")