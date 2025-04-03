# Lab 04 task `05
def count_digits_qty(num: int) -> int:
    digits = 0
    while num > 0:
        digits += 1
        num //= 10
    return digits

def if_digit_occurs(num: int, dig: int) -> bool:
    occurs = False
    while num > 0:
        if num % 10 == dig:
            occurs = True
            break
        num //= 10
    return occurs

def digit_occurrence_qty(num: int, dig: int) -> int:
    occurs_qty = 0
    while num > 0:
        if num % 10 == dig:
            occurs_qty += 1
        num //= 10
    return occurs_qty

def get_oldest_digit(num: int) -> int:
    oldest = 0
    while num > 0:
        oldest = num % 10
        num //= 10
    return oldest

def get_max_digit(num: int) -> int:
    max_dig = num % 10
    while num > 0:
        if (l_d := num % 10) > max_dig: max_dig = l_d
        num //= 10
    return max_dig

def get_min_digit(num: int) -> int:
    min_dig = num % 10
    while num > 0:
        if (l_d := num % 10) < min_dig: min_dig = l_d
        num //= 10
    return min_dig

number = 123456714

print(f"\nКількість цифр в числі {number}: {count_digits_qty(number)}")
print(f"Чи зустрічається число 3: {if_digit_occurs(number, 3)}")
print(f"Чи зустрічається число 0: {if_digit_occurs(number, 0)}")
print(f"Число 1 зустрічається {digit_occurrence_qty(number, 1)} разів")
print(f"Число 0 зустрічається {digit_occurrence_qty(number, 0)} разів")
print(f"Старша цифра: {get_oldest_digit(number)}")
print(f"Найбільша цифра: {get_max_digit(number)}")
print(f"Найменша цифра: {get_min_digit(number)}")