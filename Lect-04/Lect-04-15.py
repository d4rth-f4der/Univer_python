def print_fraction(v: float, k: int):
    """
    Виводить k дробових цифр числа v(0<=v<1)
    """
    if not(0 <= v < 1 and k > 0):
        return
    for i in range(k):
        v *= 10
        d = int(v)
        v -= d
        print(d, end="")

print_fraction(0.1235125, 4)