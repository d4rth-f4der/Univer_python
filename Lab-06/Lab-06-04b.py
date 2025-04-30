# Lab-06 Task 04 b
def input_to_int_list():
    new_list = []

    print("Вводьте цілі числа з клавіатури (натисніть Ctrl+Z або Ctrl+D для завершення):")

    while True:
        try:
            input_line = input()
            try:
                number = int(input_line)
                new_list.append(number)
            except ValueError:
                return None

        except EOFError:
            print("\nВведення завершено користувачем (Ctrl+Z/D).")
            break
        except Exception as e:
            print(f"Виникла неочікувана помилка введення: {e}")

    return new_list

my_integers = input_to_int_list()
if my_integers is not None:
    print(f"\nОтриманий список цілих чисел: {my_integers}")
else:
    print("\nВведення було неуспішним.")