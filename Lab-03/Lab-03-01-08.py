# Лабораторна 3 завдання 1 (8)

try:
    print(1, end="") # надрукується
    print(1 / 0, end="") # помилка, піде в ZeroDivisionError
except ZeroDivisionError:
    print(3, end="") # надрукується
except Exception:
    print(2 / 0, end="")
    print(4, end="")
else:
    print(5, end="")
finally:
    print(6, end="") # надрукується в кінці