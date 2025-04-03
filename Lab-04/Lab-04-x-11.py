# Lab 04 task `11
def get_n_element_of_relation(n: int) -> int:
    if n < 1:
        raise ValueError("n повинно бути більше або дорівнювати 1")
    ak = 1
    if n == 1:
        return ak

    bk = 1
    k = 1
    while k < n:
        an = bk * ak + 2 * ak
        bn = ak % bk + 2 * ak
        ak = an
        bk = bn
        k += 1
    return ak

print(get_n_element_of_relation(1))
print(get_n_element_of_relation(2))
print(get_n_element_of_relation(3))
print(get_n_element_of_relation(4))
