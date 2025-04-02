def digits_sum_iter(n: int) -> int:
    """
    Обчислює суму цифр числа
    """
    suma = 0    # suma = сума к оброблених чисел
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

print(digits_sum_iter(1234))