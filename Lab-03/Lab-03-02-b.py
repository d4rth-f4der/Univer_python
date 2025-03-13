# Лабораторна 3 завдання 2 (б)

def f(x):
    try:
        return int(1 / x)   # І виклик кине помилку ZeroDivisionError
    except TypeError:   # не опрацьовує ZeroDivisionError, вона буде опрацьована після виконання функції
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")    # І виклик друкує 3;
        return 2    # І виклик повертає 2, перекриває ZeroDivisionError

try:
    print(f(0) or f(1), end="") # f(0) повертається як 2, це вже true, тому повертається 2 а виклика f(1) не відбувається
    print(3, end="") # друкує 3
except:
    print(4, end="")