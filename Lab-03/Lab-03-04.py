# Лабораторна 3 завдання 4

def input_in_range(start_on, finish_on):
    try:
        number = int(input(f"Введіть число в діапазоні {start_on, finish_on}: "))
        if (start_on <= number <= finish_on) or (start_on >= number >= finish_on):
            return number
        else:
            print(f"Число має бути в діапазоні від {start_on} до {finish_on}")
            return input_in_range(start_on, finish_on)
    except Exception:
        print("Неправильний ввод!")
        return input_in_range(start_on, finish_on)

x = input_in_range(-5, 67)
print(f"Ваше число: {x}")