def fact_for(n):
    if n < 0: return 0

    res = 1
    for k in range(1, n + 1):
        res *= k
    return res

print(fact_for(5))