import math

x = 1.5
res = (tmp := math.sin(x)) + 1 / tmp    # оператор присвоювання :=
"""
без присвоювання:
tmp = math.sin(x)
res = tmp + 1 / tmp
"""

print(res)