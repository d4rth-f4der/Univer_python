# Лабораторна 3 завдання 1 (14)

def f(x):
    try:
        print(int(1 / x), end="") # друкує 1
    except:
        print(1, end="")
    else:
        print(2, end="") # друкує
        raise TypeError # спровокує except ззовні після завершення функції
    finally:
        print(3, end="") # друкує

try:
    f(1) # <-- виклик функції
    f(0)
except: print(4, end="") # друкує