# Lab 04 task 10-01
def get_fibonacci_by_index(index: int) -> int:
    global call_counter
    call_counter += 1
    if index <= 0:
        raise ValueError("Індекс повинен бути більшим за 0")
    elif index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return get_fibonacci_by_index(index - 1) + get_fibonacci_by_index(index - 2)

call_counter = 0
print(f"послідовність Фібоначчі до 7 символа: 0 1 1 2 3 5 8\nпошук функцією: {get_fibonacci_by_index(7)}"
      f"\nкількість викликів: {call_counter}")
print("! Ітераційний підхід для цієї задачі був би значно кращим:"
      "\nчасова складність: О(n) проти O(ф^n)"
      "\nпросторова складність: О(1) проти О(n)")