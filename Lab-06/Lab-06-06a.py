# Lab-06 Task 06 a
def input_to_int_list_qty_of(n):
    new_list = []

    print("Вводьте цілі числа з клавіатури (натисніть Ctrl+Z або Ctrl+D для завершення):")

    for _ in range(n):
        try:
            input_line = input()
            try:
                number = int(input_line)
                new_list.append(number)
            except ValueError:
                raise RuntimeError(f"Неуспішне введення: '{input_line}' не є цілим числом.")

        except EOFError:
            print("\nВведення завершено користувачем (Ctrl+Z/D).")
            break
        except Exception as e:
            raise RuntimeError(f"Виникла неочікувана помилка введення: {e}")

    return new_list



try:
    my_integers = input_to_int_list_qty_of(5)
    print(f"\nОтриманий список цілих чисел: {my_integers}")
except RuntimeError as e:
    print(f"\nВиникла помилка під час введення: {e}")