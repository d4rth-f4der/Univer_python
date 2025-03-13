# Лабораторна 3 завдання 1 (2)

try:
    print(1, end="") # надрукується
    print(1 / 0, end="") # помилка, піде в Exception
    print(2, end="")
except Exception:
    print(3, end="") # надрукується
except ZeroDivisionError:
    print(4, end="")
else:
    print(5, end="")
finally:
    print(6, end="") # надрукується в будь-якому випадку в кінці