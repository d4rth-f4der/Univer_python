# Самостійна робота 1, завдання 5
first_number = float(input("Введіть перше число (ціле або з дробовою частиною): "))
second_number = float(input("Введіть друге число (ціле або з дробовою частиною): "))
third_number = float(input("Введіть третє число (ціле або з дробовою частиною): "))

minNumber = first_number
maxNumber = first_number

if second_number < minNumber:
    minNumber = second_number
if third_number < minNumber:
    minNumber = third_number

if second_number > maxNumber:
    maxNumber = second_number
if third_number > maxNumber:
    maxNumber = third_number

print(f"""
Мінімальне число: {minNumber}"
Максимальне число: {maxNumber}""")