# Lab 04 task 02
def count_instances_of_dig_in_num(digit: int, num: int):

    if num == 0: return 0
    
    count = 0
    if num % 10 == digit: count = 1

    return count + count_instances_of_dig_in_num(digit, num // 10)

print(count_instances_of_dig_in_num(1, 134151))