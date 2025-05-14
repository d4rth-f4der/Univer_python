# Лабораторна 7, завдання 13
test_list_1 = [1, 5, 6, 2.3, 8, 11]
test_list_2 = [-2, 5, 8, 14, 6, -8]

print(f"\nПеревірка послідовності: {test_list_1}")

all_positive_1 = all(element > 0 for element in test_list_1)
print(f"  Всі елементи є додатними? {all_positive_1}")

all_integers_1 = all(isinstance(element, int) for element in test_list_1)
print(f"  Всі елементи є цілими? {all_integers_1}")

print(f"\nПеревірка послідовності: {test_list_2}")

all_positive_2 = all(element > 0 for element in test_list_2)
print(f"  Всі елементи є додатними? {all_positive_2}")

all_integers_2 = all(isinstance(element, int) for element in test_list_2)
print(f"  Всі елементи є цілими? {all_integers_2}")