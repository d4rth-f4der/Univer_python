# Lab-06 Task 09
import sys # Імпортуємо sys для можливості перевірки на EOF

def input_list_of_n_different_ints(n: int) -> list[int]:

    if not isinstance(n, int):
        raise TypeError("Кількість n має бути цілим числом.")
    elif n < 0:
        raise ValueError("Кількість n не може бути від'ємною.")
    elif n == 0:
        print("Задано n = 0. Повертаємо порожній список.")
        return []


    new_list = []
    if n == 1:
        print(f"Будь ласка, введіть {n} ціле число (Enter після кожного):")
    elif 2 <= n <= 4:
        print(f"Будь ласка, введіть {n} різних цілих числа (Enter після кожного):")
    else:
        print(f"Будь ласка, введіть {n} різних цілих чисел (Enter після кожного):")

    while len(new_list) < n:
        try:
            prompt = f"Введіть число {len(new_list) + 1} з {n}: "
            input_line = input(prompt)

            if not input_line:
                 raise RuntimeError("Неуспішне введення: введено порожній рядок.")

            try:
                number = int(input_line)
                if number not in new_list:
                    new_list.append(number)
                else:
                    print(f"Число '{number}' вже є в списку. введіть інше число.")

            except ValueError:
                raise RuntimeError(f"Неуспішне введення: '{input_line}' не є цілим числом.")

        except EOFError:
            raise RuntimeError(f"Введення завершено раніше, ніж потрібно. Введені елементи: {len(new_list)}.")
        except Exception as e:
            raise RuntimeError(f"Виникла неочікувана помилка введення: {e}")

    print(f"\nУспішно зібрано {n} різних цілих чисел.")
    return new_list

try:
    distinct_ints1 = input_list_of_n_different_ints(3)
    print(f"\nОтриманий список різних цілих чисел: {distinct_ints1}")
except (TypeError, ValueError, RuntimeError) as e:
    print(f"\nПомилка: {e}")