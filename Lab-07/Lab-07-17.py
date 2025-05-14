# Лабораторна 7, завдання 17
test_list_1 = [1, 5, 6, 2.3, 8, 11]
test_list_2 = [13, 13, 13, 13, 13, 13]

print(f"\nПеревірка послідовності: {test_list_1}")
is_stationary_1 = len(set(test_list_1)) <= 1
print(f"  Послідовність є стаціонарною? {is_stationary_1}")

print(f"\nПеревірка послідовності: {test_list_2}")
is_stationary_2 = len(set(test_list_2)) <= 1
print(f"  Послідовність є стаціонарною? {is_stationary_2}") # Очікуємо True