# Лабораторна 3 завдання 1 (16)

def f(x):
    try:
        print(int(1 / x), end="") # І виклик - друкує 1; ІІ виклик кине помилку ZeroDivisionError
    except TypeError:
        print(1, end="")
    else:
        print(2, end="") # І виклик - друкує
    finally:
        print(3, end="") # І виклик - друкує; ІІ виклик - друкує

try:
    f(1)
    f(0)
except:
    print(4, end="") # ІІ виклик друкує (ловить помилку ZeroDivisionError після завершення функції)