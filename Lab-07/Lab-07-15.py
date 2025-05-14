# Лабораторна 7, завдання 15
import math

def is_prime(n: int) -> bool:
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

test_list_1 = [7, 14, 49, 35, -3]
test_list_2 = [25, 49, 144, 81, 26]

print(f"\nПеревірка послідовності: {test_list_1}")

contains_7_1 = any(element == 7 for element in test_list_1)
print(f"  а) Послідовність містить число 7? {contains_7_1}")

contains_negative_1 = any(element < 0 for element in test_list_1)
print(f"  б) Послідовність містить від'ємні числа? {contains_negative_1}")

contains_divisible_by_13_1 = any(element % 13 == 0 for element in test_list_1)
print(f"  в) Послідовність містить хоча б одне число, що ділиться на 13? {contains_divisible_by_13_1}")

contains_prime_1 = any(is_prime(element) for element in test_list_1)
print(f"  г) Послідовність містить хоча б одне просте число? {contains_prime_1}")

print(f"\nПеревірка послідовності: {test_list_2}")

contains_7_2 = any(element == 7 for element in test_list_2)
print(f"  а) Послідовність містить число 7? {contains_7_2}")

contains_negative_2 = any(element < 0 for element in test_list_2)
print(f"  б) Послідовність містить від'ємні числа? {contains_negative_2}")

contains_divisible_by_13_2 = any(element % 13 == 0 for element in test_list_2)
print(f"  в) Послідовність містить хоча б одне число, що ділиться на 13? {contains_divisible_by_13_2}")

contains_prime_2 = any(is_prime(element) for element in test_list_2)
print(f"  г) Послідовність містить хоча б одне просте число? {contains_prime_2}")