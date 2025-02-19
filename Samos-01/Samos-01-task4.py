# Самостійна робота 1, завдання 4

first_number = 5
second_number = 14
third_number = 67

N = float(input("Введіть значення N (число, ціле або з дробовою частиною): "))

print(f"числа в діапазоні від 1 до {N}: ")

if (first_number > 1) and (first_number < N):
    print(f"{first_number}")
if (second_number > 1) and (second_number < N):
    print(f"{second_number}")
if (third_number > 1) and (third_number < N):
    print(f"{third_number}")
