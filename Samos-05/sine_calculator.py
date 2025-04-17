import math

def approx_sin_calculation(rad: float, eps: float = 1e-6) -> tuple[float, int]:

    if eps <= 0:
        raise ValueError("Точність eps має бути додатньою.")
    cur_addend = rad
    pow_sum = cur_addend
    pivot_fact = 2
    x = -rad * rad
    iterations = 0

    while math.fabs(cur_addend) >= eps:
        cur_addend *= x / (pivot_fact * (pivot_fact + 1))
        pow_sum += cur_addend
        pivot_fact += 2
        iterations += 1

    return pow_sum, iterations