# Лабораторна 3 завдання 1 (11)

def f(x):
    return 1/x # помилка ділення на 0, піде в Exception

try:
    print(f(0), end="") # <-- виклик функції з аргументом 0, що дає помилку ділення на 0
    print(1, end="")
except Exception:
    print(2, end="") # надрукується
else:
    print(3, end="")
finally:
    print(4, end="") # надрукується