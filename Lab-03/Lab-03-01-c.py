# Лабораторна 3 завдання 1 (в)

a = 1
b = 1

def f(b):
    global a
    a += 1 + b  # змінить значення зовнішнього а
    return a

def g(x):
    a = 2
    x = a + b
    return x

a = 3
b = 4
print(f(a), g(b), a, b)     # f(3) g(4) 7(після f(a)) 4