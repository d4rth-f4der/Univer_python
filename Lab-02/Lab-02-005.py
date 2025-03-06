# Лабораторна 2 завдання 5

import math
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
exp_1 = math.log(math.sqrt(a ** 2 + b ** 2))
exp_2 = math.sin((a + b) ** (1 / 7))
exp_3 = math.cos(math.cbrt(a * 12 + b ** 12))
exp_4 = 1 / math.tan(math.fabs(math.sqrt(a) - math.sqrt(b)))

print(exp_1)
print(exp_2)
print(exp_3)
print(exp_4)