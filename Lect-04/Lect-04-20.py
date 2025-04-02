def fibo(n: int) -> int:
    if n < 0:
        return -1
    f2, f1 = 0, 1
    if n == 0:
        return f2
    for _ in range(1, n):
        f2, f1 = f1, f1 + f2
    return f1

print(fibo(6))