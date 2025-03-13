# Лабораторна 3 завдання 1 (18)

def f(x):
    try:
        return int(1 / x) # І виклик поверне 1; ІІ виклик відправить до except
    except:
        print(1, end="") # ІІ виклик друкує
        return 0 # ІІ виклик поверне 0
    else:
        print(2, end="")
        return 1
    finally:
        print(3, end="") # І виклик друкує; ІІ виклик друкує;

try:
    print(f(1) and f(0), end="") # після завершення ІІ друкує 0 (1 and 0 = 0)
    print(3, end="") # друкує
except:
    print(4, end="")