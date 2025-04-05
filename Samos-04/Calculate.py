from decimal import Decimal

def calc_earned(dict_employees: dict, employee: str) -> Decimal:
    try:
        rate = dict_employees[str(employee)].get("wage") / Decimal('30')
        days_worked = dict_employees[str(employee)].get("days worked")
        return rate * days_worked
    except KeyError:
        print(f"Працівника з ім'ям '{employee}' не знайдено!")
        return Decimal('0')

def print_earned(dict_employees: dict):
    name = input("Введіть ім'я працівника: ")
    print(f"{name} заробив {calc_earned(dict_employees, name):.2f}")

def calc_and_add_earned_all(employees_dict: dict):
    keys = list(employees_dict.keys())
    for key in keys:
        earned = calc_earned(employees_dict, key)
        employees_dict[key].update({"earned": earned})