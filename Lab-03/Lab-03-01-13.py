# Лабораторна 3 завдання 1 (13)

def f(x):
    try:
        print(int(1 / x), end="") # І виклик - ділення на 0, піде в except, ІІ виклик - друкує 1
    except:
        print(1, end="") # І виклик - друкує
    else:
        print(2, end="") # II виклик - друкує
        raise TypeError # # ІI виклик - спровокує except ззовні після завершення функції
    finally:
        print(3, end="") # І виклик - друкує, ІІ виклик - друкує

try:
    f(0)
    f(1)
except:
    print(4, end="") # ІІ виклик - друкує