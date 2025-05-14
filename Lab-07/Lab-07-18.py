# Лабораторна 7, завдання 18
test_list_1 = [40, 30, 22, 12, 5, 3]
test_list_2 = [30, 25, 12, 7, 3, 1]

test_list_3 = [10, 20]
test_list_4 = [5, 10, 15]

test_list_5 = [20, 10, 5]
test_list_6 = [15, 15, 2]

print(f"\nПеревірка: {test_list_1} мажорує {test_list_2}?")
does_majorize_1 = (len(test_list_1) == len(test_list_2)
                   and all(a_element > b_element for a_element, b_element in zip(test_list_1, test_list_2)))
print(f"  Результат: {does_majorize_1}")

print(f"\nПеревірка: {test_list_3} мажорує {test_list_4}?")
# --- Використання виразу ---
does_majorize_2 = len(test_list_3) == len(test_list_4) and \
                  all(a_element > b_element for a_element, b_element in zip(test_list_3, test_list_3))
print(f"  Результат: {does_majorize_2}")

print(f"\nПеревірка: {test_list_5} мажорує {test_list_6}?")
does_majorize_3 = len(test_list_5) == len(test_list_6) and \
                  all(a_element > b_element for a_element, b_element in zip(test_list_5, test_list_6))
print(f"  Результат: {does_majorize_3}")