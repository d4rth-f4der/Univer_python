def min_arg_fact(a: int) -> int:
    """
    Return min {n / n!>a}
    """
    if a < 0:
        return 0
    n = 1
    fact = 1    # Інваріант: fact = (n-1)!
    while fact <= a:
        fact *= n
        n += 1
    return n - 1

print(min_arg_fact(119))