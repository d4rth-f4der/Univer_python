# Lab 04 task `08
def return_n_element(n: int) -> int:
    if n <= 0:
        raise ValueError("n повинно бути більше або дорівнювати 1")
    if n == 1:
        return 3
    if n == 2:
        return -2

    a1 = 3  # a(n-2)
    a2 = -2 # a(n-1)
    i = 3
    while i <= n:
        an = 3 * a2 - a1
        a1 = a2
        a2 = an
        i += 1
    return a2

def return_n_element_for(n: int) -> int:
    if n <= 0:
        raise ValueError("n повинно бути більше або дорівнювати 1")
    if n == 1:
        return 3
    if n == 2:
        return -2

    a1 = 3  # a(n-2)
    a2 = -2 # a(n-1)
    for _ in range (3, n + 1):
        an = 3 * a2 - a1
        a1 = a2
        a2 = an
    return a2

print(return_n_element(5))
print(return_n_element_for(5))