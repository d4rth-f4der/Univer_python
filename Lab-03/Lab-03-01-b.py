# Лабораторна 3 завдання 1 (б)

a = 1
b = 1

def f(a):
    a += 1
    return a

def g(x):
    x = 2 + b
    return a

a = 3   # зміна значення а
b = 4   # зміна значення b
print(f(a), g(b), a, b)     # f(3) g(4) 3 4