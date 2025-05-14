# Лабораторна 7, завдання 2
# вираз-генератор, що задає послідовність

a_gen = (i for i in range(1, 11))
b_gen = (i*i for i in range(10, -1, -1))
c_gen = (i for i in range(0, 101) if i % 2 and i % 3 and i % 5)

print("\nпослідовні цілі числа від 2 до 19 включно:")
for el in a_gen: print(el, end=' ')

print("\n\nквадрати послідовних цілих чисел від 10 до 0 включно:")
for el in b_gen: print(el, end=' ')

print("\n\nцілі числа від 0 до 100 включно, що не діляться на 2, 3 і 5:")
for el in c_gen: print(el, end=' ')

print('')