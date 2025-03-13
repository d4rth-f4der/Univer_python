# Лабораторна 3 завдання 9

def get_positive_number():
    while True:
        try:
            value = float(input("Введіть додатнє дійсне число: "))
            if value > 0:
                if value.is_integer(): return int(value)
                else: return value
            else:
                print("Число має бути додатнім!")
        except ValueError:
            print("Введено некоректні дані!")

positive_number = get_positive_number()
print(f"Ваше число: {positive_number}")