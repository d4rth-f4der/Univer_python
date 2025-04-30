# Lab-06 Task 04 а
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
                print(f"Помилка: '{input_line}' не є цілим числом. Введення припинено.")
                break

        except EOFError:
            print("\nВведення завершено користувачем (Ctrl+Z/D).")
            break
        except Exception as e:
            print(f"Виникла неочікувана помилка введення: {e}")
            break

    return new_list

my_int_list = input_to_int_list()
print(f"\nОтриманий список цілих чисел: {my_int_list}")