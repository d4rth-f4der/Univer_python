# Лабораторна 3 завдання 1 (5)
try:
    print(1, end="") # надрукується
    print(1 / 0, end="") # помилка, піде в ZeroDivisionError
    print(2, end="")
except ZeroDivisionError:
    print(3, end="") # надрукується
except:
    print(4, end="")
else:
    print(5, end="")
finally:
    print(6, end="") # надрукується в будь-якому випадку в кінці