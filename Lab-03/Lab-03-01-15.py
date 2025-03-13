# Лабораторна 3 завдання 1 (15)

def f(x):
    try:
        print(int(1 / x), end="") # кине помилку ZeroDivisionError
    except TypeError:
        print(1, end="")
    else:
        print(2, end="")
    finally:
        print(3, end="") # друкує

try:
    f(0) # <-- виклик функції
    f(1)
except:
    print(4, end="") # друкує (ловить помилку ZeroDivisionError після завершення функції)