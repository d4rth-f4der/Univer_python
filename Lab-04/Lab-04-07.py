# Lab 04 task 07
def change_twos_to_fives(num: int) -> int:
    out_number = 0
    decimal_place = 1
    while num > 0:
        inspect_digit = num % 10
        if inspect_digit == 2:
            inspect_digit = 5
        out_number += inspect_digit * decimal_place
        decimal_place *= 10
        num = num // 10
    return out_number

print(change_twos_to_fives(22436235))