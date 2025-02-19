# Імпортуємо модуль datetime
from datetime import datetime

# Початкова вартість автомобіля
initial_price = 2000000 # грн

# Введення даних
year_of_manufacture = int(input("Введіть рік випуску автомобіля: "))
current_mileage = int(input("Введіть пробіг автомобіля (у км): "))

# Розрахунок вартості
current_year = datetime.now().year
age_of_car = current_year - year_of_manufacture
depreciation = age_of_car * 0.1
final_price = initial_price * (1 - depreciation)

# Розрахунок середньорічного пробігу
if age_of_car > 0: # Уникнення ділення на 0
    average_annual_mileage = current_mileage / age_of_car
else:
    average_annual_mileage = current_mileage

# Виведення результату
print(f"""
Інформація про автомобіль:
- Рік випуску: {year_of_manufacture}
- Вік автомобіля, років: {age_of_car}
- Початкова вартість: {initial_price:.2f} грн
- Пробіг автомобіля: {current_mileage} км
- Середньорічний пробіг: {average_annual_mileage:.0f} км/рік
- Орієнтовна поточна вартість: {final_price:.2f} грн
""")