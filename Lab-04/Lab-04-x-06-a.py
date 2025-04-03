# Lab 04 task `06-a
n, m = 1, 6
while n < m:
    print(n, m)
    n += 1
    if n % 3 == 1:
        continue
    n += 1
else: print(n, m)