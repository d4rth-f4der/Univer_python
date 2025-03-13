# Лабораторна 3 завдання 2 (в)

def f(x):
    try:
        return int(1 / x)   # І виклик ділить, але не повертає із-за return в finally
    except TypeError:
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")    # І виклик друкує 3
        return 2    # І виклик повертає 2

try:
    print(f(1) or f(0), end="") # f(1) повертається як 2, це вже true, тому повертається 2 а виклика f(0) не відбувається
    print(3, end="") # друкує 3
except:
    print(4, end="")