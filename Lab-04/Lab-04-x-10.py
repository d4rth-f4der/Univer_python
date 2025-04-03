# Lab 04 task `10
def find_first_element_greater_than(m: int) -> int:
    a0 = 1
    if m < a0: return a0

    a1 = 1
    an = 2 * a1 + 3 * a0
    if m < an: return an

    while m >= an:
        a0 = a1
        a1 = an
        an = 2 * a1 + 3 * a0
    return an

print(find_first_element_greater_than(0))
print(find_first_element_greater_than(1))
print(find_first_element_greater_than(5))