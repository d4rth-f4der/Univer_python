# Самостійна робота 4
import EmployeeInput
import Calculate
import EmployeeOutput

def employees_dict_menu(empl_dic: dict):
    while True:
        try:
            input_var = int(input("""\nЩо бажаєте зробити?
1 - додати працівника
2 - змінити запис про працівника
3 - видалити запис про працівника
4 - вивести імена працівників (рекурсивна функція)
5 - вивести всю інформацію про працівників
6 - обчислити зароблені гроші для працівника
7 - порахувати скільки заробили всі працівники і додати в словник
0 - завершити роботу
> """))
            if input_var == 1: EmployeeInput.input_employee(empl_dic)
            elif input_var == 2: EmployeeInput.modify_employee(empl_dic)
            elif input_var == 3: EmployeeInput.delete_employee(empl_dic)
            elif input_var == 4: EmployeeOutput.print_employees_names_recursive(empl_dic)
            elif input_var == 5: EmployeeOutput.print_all_employees_info(empl_dic)
            elif input_var == 6: Calculate.print_earned(empl_dic)
            elif input_var == 7: Calculate.calc_and_add_earned_all(empl_dic)
            elif input_var == 0: break
            else: print("Неправильний ввод!")
        except Exception: print("Неправильний ввод!")

employees = {}
employees_dict_menu(employees)