def fact_iter(n: int) -> int:
    if n < 0:
        return 0

    res = 1
    k = 1
    while k <= n:
        res *= k
        k += 1

    return res

print(fact_iter(5))