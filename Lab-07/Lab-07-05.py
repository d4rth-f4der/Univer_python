# Лабораторна 7, завдання 5
import random

# ФУНКЦІЇ ГЕНЕРАЦІЇ ПОСЛІДОВНОСТЕЙ
# ТА ОТРИМАННЯ ДОВЖИНИ ПОСЛІДОВНОСТІ ЧЕРЕЗ ІТЕРАТОР
# ДЛЯ ВИКОРИСТАННЯ В ЗАВДАННЯХ:

MAX_FINITE_LENGTH = 300
VALUE_RANGE_START = -50
VALUE_RANGE_END = 50

def random_integer_sequence_generator(length, value_range_start, value_range_end):
    count = 0
    while count < length:
        yield random.randint(value_range_start, value_range_end)
        count += 1

def get_iterator_length(iterator):
    count = 0
    try:
        while True:
            next(iterator)
            count += 1
    except StopIteration:
        pass
    return count

def prepare_random_sequence_for_task(max_length, value_start, value_end):
    random_seq_len = random.randint(1, max_length)
    print(f"(Випадково згенерована довжина послідовності: {random_seq_len})")
    temp_source_for_length = random_integer_sequence_generator(random_seq_len, value_start, value_end)
    actual_length = get_iterator_length(temp_source_for_length)
    print(f"Визначена довжина послідовності за допомогою ітератора: {actual_length}")
    fresh_source = random_integer_sequence_generator(actual_length, value_start, value_end)
    return fresh_source, actual_length

# ФУНКЦІЇ ЗАВДАНЬ:

def gen_5a_1st_half_incl_center(sequence, L):
    stop_index = L // 2 + (1 if L % 2 != 0 else 0)
    index = 0
    for element in sequence:
        if index < stop_index:
            yield element
        else:
            break
        index += 1

def gen_5b_1st_half_excl_center(sequence, L):
    stop_index = L // 2
    index = 0
    for element in sequence:
        if index < stop_index:
            yield element
        else:
            break
        index += 1

def gen_5c_first_third(sequence, L):
    stop_index = L // 3
    index = 0
    for element in sequence:
        if index < stop_index:
            yield element
        else:
            break
        index += 1

def gen_5d_2nd_half_incl_center(sequence, L):
    start_index = L // 2
    index = 0
    for element in sequence:
        if index >= start_index:
            yield element
        index += 1

def gen_5e_2nd_half_excl_center(sequence, L):
    start_index = L // 2 + (1 if L % 2 != 0 else 0)
    index = 0
    for element in sequence:
        if index >= start_index:
            yield element
        index += 1

def gen_5f_second_third(sequence, L):
    start_index = L // 3
    stop_index = 2 * L // 3
    index = 0
    for element in sequence:
        if start_index <= index < stop_index:
            yield element
        elif index >= stop_index: break
        index += 1

def gen_5g_each_third(sequence, L):
    index = 0
    for element in sequence:
        if index % 3 == 0:
            yield element
        index += 1

def gen_5h_each_third_back(sequence, L):
    every_third_elements = []
    index = 0
    for element in sequence:
        if index % 3 == 0:
            every_third_elements.append(element)
        index += 1

    for element in reversed(every_third_elements):
        yield element

# ФУНКЦІЇ ВИВОДУ/ВИКОНАННЯ:

def exec_print_5a():
    source_5a, sequence_length_5a = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5a = gen_5a_1st_half_incl_center(source_5a, sequence_length_5a)
    start_idx_5a = 0
    end_idx_5a = sequence_length_5a // 2 + (1 if sequence_length_5a % 2 != 0 else 0)
    print(f"Перша половина (з {start_idx_5a} до {end_idx_5a - 1} включно, {end_idx_5a} елементів, центр вкл):")
    for element in gen_5a:
        print(element, end=' ')
    print('\n')

def exec_print_5b():
    source_5b, sequence_length_5b = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5b = gen_5b_1st_half_excl_center(source_5b, sequence_length_5b)
    start_idx_5b = 0
    end_idx_5b = sequence_length_5b // 2
    print(f"Перша половина (з {start_idx_5b} до {end_idx_5b - 1} включно, {end_idx_5b} елементів, центр !НЕ! вкл):")
    for element in gen_5b:
        print(element, end=' ')
    print('\n')

def exec_print_5c():
    source_5c, sequence_length_5c = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5c = gen_5c_first_third(source_5c, sequence_length_5c)
    start_idx_5c = 0
    end_idx_5c = sequence_length_5c // 3
    print(f"Перша третина (з {start_idx_5c} до {end_idx_5c - 1} включно, {end_idx_5c} елементів:")
    for element in gen_5c:
        print(element, end=' ')
    print('\n')

def exec_print_5d():
    source_5d, sequence_length_5d = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5d = gen_5d_2nd_half_incl_center(source_5d, sequence_length_5d)
    start_idx_5d = sequence_length_5d // 2
    print(f"Друга половина (з {start_idx_5d} до {sequence_length_5d - 1} включно, {sequence_length_5d - start_idx_5d} елементів, центр вкл)")
    for element in gen_5d:
        print(element, end=' ')
    print('\n')

def exec_print_5e():
    source_5e, sequence_length_5e = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5e = gen_5e_2nd_half_excl_center(source_5e, sequence_length_5e)
    start_idx_5e = sequence_length_5e // 2 + (1 if sequence_length_5e % 2 != 0 else 0)
    print(f"Друга половина (з {start_idx_5e} до {sequence_length_5e-1} включно, {sequence_length_5e - start_idx_5e} елементів, центр !НЕ! вкл):")
    for element in gen_5e:
        print(element, end=' ')
    print('\n')

def exec_print_5f():
    source_5f, sequence_length_5f = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5f = gen_5f_second_third(source_5f, sequence_length_5f)
    start_idx_5f = sequence_length_5f // 3
    end_idx_5f = 2 * sequence_length_5f // 3
    print(f"Друга третина (з {start_idx_5f} до {end_idx_5f - 1} включно, {end_idx_5f - start_idx_5f} елементів:")
    for element in gen_5f:
        print(element, end=' ')
    print('\n')

def exec_print_5g():
    source_5g, sequence_length_5g = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5g = gen_5g_each_third(source_5g, sequence_length_5g)
    print(f"Кожен третій елемент послідовності з {sequence_length_5g} елементів:")
    for element in gen_5g:
        print(element, end=' ')
    print('\n')

def exec_print_5h():
    source_5h, sequence_length_5h = prepare_random_sequence_for_task(MAX_FINITE_LENGTH, VALUE_RANGE_START, VALUE_RANGE_END)
    gen_5h = gen_5h_each_third_back(source_5h, sequence_length_5h)
    print(f"Кожен третій елемент послідовності з {sequence_length_5h} елементів в оберненому порядку:")
    for element in gen_5h:
        print(element, end=' ')
    print('\n')

exec_print_5a()
exec_print_5b()
exec_print_5c()
exec_print_5d()
exec_print_5e()
exec_print_5f()
exec_print_5g()
exec_print_5h()