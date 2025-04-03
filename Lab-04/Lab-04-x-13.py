# Lab 04 task 13
def reverse_number(num: int) -> int:
    rev_num = 0
    while num > 0:
        rev_num *= 10
        rev_num += num % 10
        num //= 10
    return rev_num

print(reverse_number(102340))