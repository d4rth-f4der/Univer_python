# Lab 04 task 06
def make_number_from_digits_squares(num: int) -> int:
    out_number = 0
    decimal_place = 1
    while num > 0:
        out_number += (num % 10)**2 * decimal_place
        if (num % 10)**2 < 10: decimal_place *= 10
        else: decimal_place *= 100
        num = num // 10

    return out_number

print(make_number_from_digits_squares(15633))