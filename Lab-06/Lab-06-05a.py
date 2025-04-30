# Lab-06 Task 05 a
def append_to_int_list(init_list):
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
            init_list.extend(new_list)
            break
        except Exception as e:
            print(f"Виникла неочікувана помилка введення: {e}")
            break

my_int_list = [1, 5, 8]
append_to_int_list(my_int_list)
print(f"\nМодифікований список цілих чисел: {my_int_list}")