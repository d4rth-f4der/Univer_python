# Lab 04 task 01
def reverse_number(num: int, reversed_num: int = 0) -> int:
    if num == 0: return reversed_num

    digit = num % 10
    reversed_num = reversed_num * 10 + digit

    return reverse_number(num // 10, reversed_num)

print(reverse_number(12340))