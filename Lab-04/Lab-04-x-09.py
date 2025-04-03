# Lab 04 task `09
def get_first_fibonacci_greater_than(num: int) -> int:
    first_fib = 0
    second_fib = 1
    while second_fib <= num:
        temp_first = first_fib
        first_fib = second_fib
        second_fib = temp_first + second_fib
    return second_fib

print(get_first_fibonacci_greater_than(8))