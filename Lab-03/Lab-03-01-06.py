# Лабораторна 3 завдання 1 (6)

try:
    print(1, end="") # надрукується
except ZeroDivisionError:
    print(2, end="")
except:
    print(3, end="")
else:
    print(4, end="") # надрукується
finally:
    print(5, end="") # надрукується в будь-якому випадку в кінці