# Лабораторна 7, завдання 3
# вираз-генератор, що задає послідовність
import math
import random

def endless_ints_from_zero():
    i = 0
    while True:
        yield i
        i += 1

def infinite_random_integers():
    while True:
        yield random.randint(-1000, 1000)

def a_gen_even_from_sequence(sequence):
    even_int_gen = (x for x in sequence if x % 2 == 0)
    return even_int_gen

def b_gen_not_divide_2_3_5_from_seq(sequence):
    not_div235_gen = (x for x in sequence if x % 2 and x % 3 and x % 5)
    return not_div235_gen

def c_gen_greater_than(sequence, num: int):
    gr_than_gen = (x for x in sequence if x > num)
    return gr_than_gen

def d_gen_positive_ints_from_seq(sequence):
    pos_int_gen = (x for x in sequence if x > 0)
    return pos_int_gen

def if_is_prime(n: int) -> bool: # Перевірка чи число просте
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(math.sqrt(n))
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True

def e_gen_if_prime(sequence):
    if_prime_gen = (x for x in sequence if if_is_prime(x))
    return if_prime_gen

def is_perfect_square_v2(n: int) -> bool:
    if n < 0:
        return False
    sq_root = math.sqrt(n)
    return sq_root.is_integer()

def f_gen_if_perfect_square(sequence):
    if_perf_sq = (x for x in sequence if is_perfect_square_v2(x))
    return if_perf_sq

long_sequence = endless_ints_from_zero()
print("\nПерші 10 елементів, що діляться на 2 (з нескінченної послідовності 0 -> inf):")
gen_evn = a_gen_even_from_sequence(long_sequence) # фільтр краще застосувати 1 раз перед ітераціями
for _ in range(10):
    print(next(gen_evn), end=' ')

long_sequence = endless_ints_from_zero()
print("\n\nПерші 10 елементів, що не діляться на 2, 3 і 5 (з нескінченної послідовності 0 -> inf):")
gen_not_div235 = b_gen_not_divide_2_3_5_from_seq(long_sequence)
for _ in range(10):
    print(next(gen_not_div235), end=' ')

long_sequence = infinite_random_integers()
print("\n\nПерші 10 елементів більше 500 (з нескінченної послідовності випадкових цілих від -1000 до 1000):")
gen_gt_th = c_gen_greater_than(long_sequence, 500)
for _ in range(10):
    print(next(gen_gt_th), end=' ')

long_sequence = infinite_random_integers()
print("\n\nПерші 10 додатніх елементів (з нескінченної послідовності випадкових цілих від -1000 до 1000):")
gen_pos_int = d_gen_positive_ints_from_seq(long_sequence)
for _ in range(10):
    print(next(gen_pos_int), end=' ')

long_sequence = infinite_random_integers()
print("\n\nПерші 10 простих чисел (з нескінченної послідовності випадкових цілих від -1000 до 1000):")
gen_prime = e_gen_if_prime(long_sequence)
for _ in range(10):
    print(next(gen_prime), end=' ')

long_sequence = infinite_random_integers()
print("\n\nПерші 10 точних квадратів (з нескінченної послідовності випадкових цілих від -1000 до 1000):")
gen_perf_sq = f_gen_if_perfect_square(long_sequence)
for _ in range(10):
    print(next(gen_perf_sq), end=' ')