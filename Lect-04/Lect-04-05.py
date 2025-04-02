def digits_sum(n: int) -> int:
    if n < 0:
        return 0

    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

print(digits_sum(1234))