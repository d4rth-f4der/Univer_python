# Lab 04 task 09
def take_every_second_digit(num: int) -> int:
    out_number = 0
    decimal_place = 1

    while num > 0:
        inspect_digit = num % 10
        out_number += inspect_digit * decimal_place
        decimal_place *= 10
        num = num // 100
    return out_number

print(take_every_second_digit(1234567))