def find_digit(n: int, b: int) -> bool:
    if n <= 0 or b < 0:
        return False
    while n > 0 and n % 10 != b:
        n //= 10
    return n > 0

print(find_digit(145, 5))