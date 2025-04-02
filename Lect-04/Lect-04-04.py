def min_arg_fact(a: int) -> int:
    if a < 0:
        return 0
    n = 1
    fact = 1
    while fact <= a:
        fact *= n
        n += 1

    return n-1

print(min_arg_fact(119))