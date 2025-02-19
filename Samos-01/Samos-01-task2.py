# Самостійна робота 1, завдання 2

import math

x = float(input("Введіть значення х (число, ціле або з дробовою частиною): "))
t = int(1)

Z = (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x)

print(f"{Z:.2f}")