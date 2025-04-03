# Lab-04-05
def bisection_method(func, a: int, b: int, tolerance=1e-15, max_iterations=100):

    if func(a) * func(b) >= 0:
        print("Помилка: Значення a та b мають бути з різними знаками")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        mid = (a + b) / 2
        f_mid = func(mid)

        if f_mid == 0:
            return mid

        elif func(a) * f_mid < 0:
            b = mid
        else:
            a = mid

        iteration += 1

    return (a + b) / 2

def my_function(x): return x**2 - 9
lower_bound_x = 1
upper_bound_x = 4

root = bisection_method(my_function, lower_bound_x, upper_bound_x)

if root is not None:
    print(f"Наближений корінь функції (х для f(x) = 0))"
          f"на відрізку [{lower_bound_x}, {upper_bound_x}]: {root}")
    print(f"Значення функції в цій точці: {my_function(root)}")