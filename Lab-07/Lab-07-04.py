# Лабораторна 7, завдання 4
# вираз-генератор, що задає підпослідовність
import random

def mixed_types_generator():
    while True:
        yield random.randint(-1000, 1000)                                          # Ціле число (int)
        yield random.randint(-1000, 1000) + 0.5                                    # Дійсне число (float)
        yield f"text_{random.randint(-1000, 1000)}"                                # Рядок (str)
        yield [random.randint(-1000, 1000)]                                        # Список (list)
        yield (random.randint(-1000, 1000), random.randint(-1000, 1000))        # Кортеж (tuple)
        yield {random.randint(-1000, 1000): random.randint(-1000, 1000)}        # Словник (dict)
        yield {random.randint(-1000, 1000), random.randint(-1000, 1000)}        # Множина (set)
        yield None                                                                    # Тип NoneType

def a_gen_is_int(sequence):
    is_int_gen = (x for x in sequence if isinstance(x, int))
    return is_int_gen

def b_gen_is_float(sequence):
    is_float_gen = (x for x in sequence if isinstance(x, float))
    return is_float_gen

def c_gen_not_float(sequence):
    not_float_gen = (x for x in sequence if not isinstance(x, float))
    return not_float_gen

def d_gen_not_str(sequence):
    not_str_gen = (x for x in sequence if not isinstance(x, str))
    return not_str_gen

mixed_source = mixed_types_generator()
print("\nПерші 10 елементів типу int (з послідовності різних типів):")
is_int_gen = a_gen_is_int(mixed_source)
for _ in range(10):
    print(next(is_int_gen), end=' ')

mixed_source = mixed_types_generator()
print("\n\nПерші 10 елементів типу float (з послідовності різних типів):")
is_float_gen = b_gen_is_float(mixed_source)
for _ in range(10):
    print(next(is_float_gen), end=' ')

mixed_source = mixed_types_generator()
print("\n\nПерші 10 елементів, що не є float (з послідовності різних типів):")
not_float_gen = c_gen_not_float(mixed_source)
for _ in range(10):
    print(next(not_float_gen), end=' ')

mixed_source = mixed_types_generator()
print("\n\nПерші 10 елементів, що не є str (з послідовності різних типів):")
not_str_gen = d_gen_not_str(mixed_source)
for _ in range(10):
    print(next(not_str_gen), end=' ')

print('')