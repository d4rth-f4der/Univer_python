# Лабораторна 3 завдання 3 (в)

def f(x):
    try:
        return int(1 / x)   # І виклик повертає 1
    except TypeError:
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")    # друкує 3

try:
    print(f(1) or f(0), end="") # після обчислення f(1) відразу друкує 1 (1 = True)
    print(3, end="")    # друкує 3
except:
    print(4, end="")