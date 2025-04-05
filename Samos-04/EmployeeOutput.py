def print_employees_names_recursive(empl_dict: dict, index=0):
    keys = list(empl_dict.keys())
    if index < len(keys):
        print(keys[index])
        print_employees_names_recursive(empl_dict, index + 1)

def print_employee_info(employees_dict: dict, emp_name: str):
    try:
        print(f'{emp_name} - ставка: {employees_dict[str(emp_name)].get("wage")}, '
              f'днів працював: {employees_dict[str(emp_name)].get("days worked")}')
        if "earned" in employees_dict[str(emp_name)]:
            print(f'заробив: {employees_dict[str(emp_name)].get("earned"):.2f}')
    except KeyError:
        print(f"В списку немає співробітника {emp_name}!")

def print_all_employees_info(employ_dict: dict):
    keys = list(employ_dict.keys())
    for key in keys:
        print_employee_info(employ_dict, key)