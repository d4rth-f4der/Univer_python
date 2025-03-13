# Лабораторна 3 завдання 1 (10)

try:
    print(1, end="") # надрукується
except ZeroDivisionError:
    print(3, end="")
except Exception:
    print(4, end="")
else:
    print(1 / 0, end="") # виб'є помилку
    print(5, end="")
finally:
    print(6, end="") # надрукується