# Lab-06 Task 07
def input_to_list_typed(element_type):
    new_list = []
    print(f"Вводьте значення типу {element_type.__name__} з клавіатури; введіть .end для завершення):")

    while True:
        try:
            input_line = input()
            if input_line == ".end": break

            try:
                element = element_type(input_line)
                new_list.append(element)
            except (ValueError, TypeError):
                print(f"Попередження: '{input_line}' не може бути перетворено до типу"
                      f"{element_type.__name__} і було проігноровано.")
                pass

        except EOFError:
            print("\nВведення завершено користувачем (Ctrl+Z/D).")
            break
        except Exception as e:
            print(f"Виникла неочікувана помилка введення: {e}")
            break

    return new_list

print("введення цілих чисел:")
int_list = input_to_list_typed(int)
print(f"\nОтриманий список int: {int_list}")

print("\n" + "="*30 + "\n")

print("введення дійсних чисел")
float_list = input_to_list_typed(float)
print(f"\nОтриманий список float: {float_list}")

print("\n" + "="*30 + "\n")

print("введення рядків")
str_list = input_to_list_typed(str)
print(f"\nОтриманий список str: {str_list}")