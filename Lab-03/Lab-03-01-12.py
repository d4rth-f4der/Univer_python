# Лабораторна 3 завдання 1 (12)

def f(x):
    y = 1/x # помилка ділення на 0, піде в Exception
    print(0, end="")

try:
    f(0) # <-- виклик функції з аргументом 0, що дає помилку ділення на 0
    print(1, end="")
except Exception:
    print(2, end="") # надрукується
else:
    print(3, end="")
finally:
    print(4, end="") # надрукується