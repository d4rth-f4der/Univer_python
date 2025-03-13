# Лабораторна 3 завдання 3 (б)

def f(x):
    try:
        return int(1 / x)   # І виклик кине помилку ZeroDivisionError
    except TypeError:   # не опрацьовує ZeroDivisionError, вона буде опрацьована після виконання функції
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")    # друкує 3

try:
    print(f(0) or f(1), end="") # f(0) повертає ZeroDivisionError, це переводить нас до except
    print(3, end="")
except:
    print(4, end="")    # опрацьовує помилку ZeroDivisionError після виклику f(0) => друкує 4