from decimal import Decimal

def get_name() -> str:
    while True:
        emp_name = input("Введіть ім'я: ").strip()
        if emp_name:
            break
        else:
            print("Ім'я не може бути порожнім")
    return emp_name

def get_wage() -> Decimal:
    while True:
        try:
            emp_wage = Decimal(input("Введіть зар.платню: ").strip())
            if emp_wage <= 0:
                print("Має бути більше 0!")
            else:
                break
        except Exception:
            print("Має бути числом!")

    return emp_wage

def get_days() -> int:
    while True:
        try:
            worked_days = int(input("Введіть кількість днів: ").strip())
            if worked_days < 0: print("Кількість днів не може бути від'ємною!")
            else: break
        except ValueError:
            print("Має бути цілим числом!")
    return worked_days

def input_employee(employees_dict: dict):
    while True:
        name = get_name()
        if name in employees_dict:
            print("Вже є такий працівник!")
        else: break
    employees_dict.update({name: {"wage": get_wage(), "days worked": get_days()}})

def modify_employee(employees_dict: dict):
    name = get_name()
    if name not in employees_dict:
        print("Такого працівника немає!")
        return None
    employees_dict.update({name: {"wage": get_wage(), "days worked": get_days()}})
    if "earned" in employees_dict[name]: employees_dict[name].pop("earned")

def delete_employee(employees_dict: dict):
    name = get_name()
    if name in employees_dict:
        employees_dict.pop(name)
        print(f"Працівника {name} видалено")
    else: print(f"Немає працівника {name}!")