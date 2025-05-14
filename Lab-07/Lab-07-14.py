# Лабораторна 7, завдання 14
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

test_list_1 = [7, 14, 49, 35]
test_list_2 = [25, 49, 144, 81]
test_list_3 = [7, 13, 31, 23]

given_number = 8

print(f"\nПеревірка послідовності: {test_list_1}")
all_divisible_by_7_1 = all(element % 7 == 0 for element in test_list_1)
print(f"  а) Всі елементи діляться на 7? {all_divisible_by_7_1}")

all_greater_than_given_1 = all(element > given_number for element in test_list_1)
print(f"  б) Всі елементи більші за {given_number}? {all_greater_than_given_1}")

# Використовуємо умова >=0 та math.isqrt
all_perfect_squares_1 = all(element >= 0 and math.isqrt(element)**2 == element for element in test_list_1)
print(f"  в) Всі елементи є точними квадратами? {all_perfect_squares_1}")

all_prime_1 = all(is_prime(element) for element in test_list_1)
print(f"  г) Всі елементи є простими числами? {all_prime_1}")

print(f"\nПеревірка послідовності: {test_list_2}")
all_divisible_by_7_1 = all(element % 7 == 0 for element in test_list_2)
print(f"  а) Всі елементи діляться на 7? {all_divisible_by_7_1}")

all_greater_than_given_1 = all(element > given_number for element in test_list_2)
print(f"  б) Всі елементи більші за {given_number}? {all_greater_than_given_1}")

# Використовуємо умова >=0 та math.isqrt
all_perfect_squares_1 = all(element >= 0 and math.isqrt(element)**2 == element for element in test_list_2)
print(f"  в) Всі елементи є точними квадратами? {all_perfect_squares_1}")

all_prime_1 = all(is_prime(element) for element in test_list_2)
print(f"  г) Всі елементи є простими числами? {all_prime_1}")

print(f"\nПеревірка послідовності: {test_list_3}")
all_divisible_by_7_1 = all(element % 7 == 0 for element in test_list_3)
print(f"  а) Всі елементи діляться на 7? {all_divisible_by_7_1}")

all_greater_than_given_1 = all(element > given_number for element in test_list_3)
print(f"  б) Всі елементи більші за {given_number}? {all_greater_than_given_1}")

# Використовуємо умова >=0 та math.isqrt
all_perfect_squares_1 = all(element >= 0 and math.isqrt(element)**2 == element for element in test_list_3)
print(f"  в) Всі елементи є точними квадратами? {all_perfect_squares_1}")

all_prime_1 = all(is_prime(element) for element in test_list_3)
print(f"  г) Всі елементи є простими числами? {all_prime_1}")


