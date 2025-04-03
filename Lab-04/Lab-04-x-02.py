# Lab 04 task `02
def find_minimal_as_great_factorial_argument(a: int) -> int:
    if a <= 1: return 0
    elif a > 1:
        factorial_arg = 2
        factorial = 2
        while factorial < a:
            factorial_arg += 1
            factorial *= factorial_arg
        return factorial_arg

print(find_minimal_as_great_factorial_argument(120))
print(find_minimal_as_great_factorial_argument(121))