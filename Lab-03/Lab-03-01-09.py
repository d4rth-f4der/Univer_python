# Лабораторна 3 завдання 1 (9)

try:
    print(1, end="") # надрукується
    print(1 / 0, end="") # помилка, піде в ZeroDivisionError
except ZeroDivisionError:
    print(2 / 0, end="") # помилка при обробці помилки, виб'є помилку
    print(3, end="")
except Exception:
    print(4, end="")
else:
    print(5, end="")
finally:
    print(6, end="") # надрукується