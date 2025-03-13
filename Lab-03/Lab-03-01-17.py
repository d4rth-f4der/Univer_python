# Лабораторна 3 завдання 1 (17)

def f(x):
    try:
        return int(1 / x) # І виклик обчислить, але не поверне (в finally є return); ІІ виклик відправить до except
    except:
        print(1, end="") # ІІ виклик - друкує
        return 0 # ІІ виклик не поверне (в finally є return)
    else:
        print(2, end="")
        return 1
    finally:
        print(3, end="") # І виклик - друкує; ІІ виклик - друкує
        return 2 # І виклик - повертає; ІІ виклик - повертає

try:
    print(f(1) and f(0), end="") # після завершення ІІ друкує 2 (2 and 2 = 2 (останній, якщо обидва true))
    print(3, end="") # друкує
except:
    print(4, end="")
