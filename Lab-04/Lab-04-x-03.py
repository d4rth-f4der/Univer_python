# Lab 04 task `03
def find_max_of_fact_not_bigger_than(a: int) -> int:
    if a < 1:
        raise ValueError("Мінімальний коректний факторіал - 0!=1")
    else:
        factorial_arg = 0
        factorial = 1
        while factorial <= a:
            factorial_arg += 1
            factorial *= factorial_arg
        return factorial_arg - 1

print(find_max_of_fact_not_bigger_than(119))
print(find_max_of_fact_not_bigger_than(120))