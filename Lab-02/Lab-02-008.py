# Лабораторна 2 завдання 8
import math

res = math.sqrt(2)
res_dot_digits = int(input("Для результату обчислення sqrt(2) введіть кількість знаків після коми: "))
res_rounded = round(res, res_dot_digits)
print(f'a) sqrt(2) = {res_rounded}')


res_b = 2.5 ** 1.6
res_b_dot_digits = int(input("Для результату обчислення 2.5^1.6 введіть кількість знаків після коми: "))
res_b_rounded = round(res_b, res_b_dot_digits)
print(f'б) 2.5^1.6 = {res_b_rounded}')

res_c = math.pi + math.e
res_c_dot_digits = int(input("Для результату обчислення Pi + e введіть кількість знаків після коми: "))
res_c_rounded = round(res_c, res_c_dot_digits)
print(f'c) Pi + e = {res_c_rounded}')