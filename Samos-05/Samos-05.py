# Самостійна робота 5
import math

# степеневий ряд для функції синуса: sin(x) = x - (x³ / 3!) + (x⁵ / 5!) - (x⁷ / 7!) + (x⁹ / 9!) + ...

def approx_sin(rad: float, eps: float = 1e-6) -> float:


    if eps <= 0:
        raise ValueError("Точність eps має бути додатньою.")
    cur_addend = rad
    pow_sum = cur_addend
    pivot_fact = 2
    x = -rad * rad

    while math.fabs(cur_addend) >= eps:
        cur_addend *= x / (pivot_fact * (pivot_fact +1))
        pow_sum += cur_addend
        pivot_fact += 2

    return pow_sum

print(approx_sin(math.radians(30), 1e-10))
print(approx_sin(713))