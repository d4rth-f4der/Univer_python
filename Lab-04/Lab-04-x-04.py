# Lab 04 task `04
import math


def calculate_log_base_n_arg_m(base: int, arg: int):
    try:
        return math.log(arg, base)
    except Exception as error:
        print(f"Помилка {error}, введіть коректні числа")

print(calculate_log_base_n_arg_m(2, 4))