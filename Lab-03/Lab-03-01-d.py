# Лабораторна 3 завдання 1 (г)

a = 1
b = 2
c = b   # c = 2

def f(x, y):
    x += 1
    y += 2
    c = a + b
    return x * y

b = 3   # зміна значення b
print(a, b, c)  # 1 3 2
print(f(a,b), a, b, c) # f(1,3)=10 1 3 2