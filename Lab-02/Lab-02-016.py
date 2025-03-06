# Лабораторна 2 завдання 16
import math

def day_month_year_format(in_day, in_month, in_year):
    if in_day.isdigit() and in_month.isdigit() and in_year.isdigit():
        day = int(in_day)
        month = int(in_month)
        year = int(in_year)
        if month < 1 or month > 12:
            print("Неправильно введено місяць")
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 1 or day > 31:
                print("Неправильно введено день")
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                print("Неправильно введено день")
        if month == 2 and (math.fabs(year) % 4) == 0:
            if day < 1 or day > 29:
                print("Неправильно введено день")
        if month == 2 and (math.fabs(year) % 4) != 0:
            if day < 1 or day > 28:
                print("Неправильно введено день")
        else:
            print(f"дата в форматі dd.mm.yy: {day:0>2}.{month:0>2}.{year % 100:0>2}")
    else:
        print("Дані введено некоректно")


input_day = input("Введіть день місяця (число): ")
input_month = input("Введіть місяць (число): ")
input_year = input("Введіть рік: ")

day_month_year_format(input_day, input_month, input_year)
