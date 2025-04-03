# Lab 04 task `01-d
i, n, m = 1, 2, 1
while n < m:
    print(i, n, m)
    i += 1
    n *= i
    m *= 2
else:
    print(i, n, m)