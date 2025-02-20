# Лабораторна робота 1, завдання 12
# Записати вираз для обчислення значень

from decimal import Decimal

# a)
upper_value = Decimal('10.001') ** 345 * Decimal('13.001') ** 149
lower_value = Decimal('9.001') ** 155 * Decimal('11.001') ** 179

print(upper_value / lower_value)

# б)
upper_value = Decimal('10.001') ** 345 * Decimal('13.001') ** 249
lower_value = Decimal('9.001') ** 355 * Decimal('11.001') ** 269

print(upper_value / lower_value)

#в)
print((20 / 3) * (12 / 5) * (11 / 7))

#г)
print((12.11 * 71) / (3.5 * 9))