# num_students = input("Введіть кількість студентів: ")
# print(f"Ви ввели: {num_students}")

"""students = [] # Порожній список для збереження імен студентів

for _ in range(num_students):
    while True:
        name = input("Введіть ім'я студента: ").strip()
        if name:
            students.append(name)  # Додаємо ім'я у список
            break # Вихід з циклу, якщо ім'я введено правильно
        else:
            print("Ім'я не може бути порожнім!")

    while True:
        try:
            scores = list(map(int, input(f"Введіть оцінки {name} через пробіл: ").split()))
            if not scores:
                print("Оцінки не можуть бути порожніми!")
            elif any(score < 0 or score > 100 for score in scores):
                print("Оцінки мають бути в межах 0-100!")
            else:
                students[name] = scores
                break
        except ValueError:
            print("Помилка! Введіть числа, через пробіл.")

print("Список студентів:", students)

grades = {} # Створюємо словник для збереження оцінок

for student in students:
    while True:
        try:
            scores = list(map(int, input(f"Введіть оцінки {student} через пробіл: ").split()))
            if not scores: # Перевіряємо, чи список не порожній
                print("Оцінки не можуть бути порожніми!")
            elif any(score < 0 or score > 100 for score in scores):
                print("Оцінки мають бути в межах 0-100!")
            else:
                grades[student] = scores
                break # Вихід з циклу, якщо оцінки введено правильно
        except ValueError:
            print("Помилка! Введіть числа, через пробіл.")

    grades[student] = scores # Зберігаємо оцінки у словнику

print("\nРезультати виведення: ")
print(grades)"""

def get_student_data():
    """Функція для введення даних студентів (ПІБ та оцінки)"""
    students = {}

    while True:
        try:
            num_students = int(input("Введіть кількість студентів: "))
            if num_students <= 0:
                print("Кількість студентів має бути більше 0!")
            else:
                break
        except ValueError:
            print("Помилка! Введіть ціле число")

    for _ in range(num_students):
        while True:
            name = input("Введіть ім'я студента: ").strip()
            if name:
                break
            else:
                print("Ім'я не може бути порожнім!")

        while True:
            try:
                scores = list(map(int, input(f"Введіть оцінки {name} через пробіл: ").split()))
                if not scores:
                    print("Оцінки не можуть бути порожніми!")
                elif any(score < 0 or score > 100 for score in scores):
                    print("Оцінки мають бути в межах 0-100!")
                else:
                    students[name] = scores
                    break
            except ValueError:
                print("Помилка! Введіть числа, через пробіл.")

    return students

# students_data = get_student_data()
# print("\nЗібрані дані:", students_data)

def calculate_average(grades_dict):
    """Обчислює середній бал групи."""
    total_sum = 0
    total_count = 0

    for scores in grades_dict.values():
        total_sum += sum(scores)
        total_count += len(scores)

    if total_count == 0:
        return 0 # Уникаємо ділення на нуль

    return total_sum / total_count

def find_students_below_average(grades_dict, avg):
    """Знаходить студентів із середнім балом нижче групового"""
    below_avg_students = {}

    for student, scores in grades_dict.items():
        student_avg = sum(scores) / len(scores)
        if student_avg < avg:
            below_avg_students[student] = student_avg

    return below_avg_students

students_data = get_student_data()
group_avg = calculate_average(students_data)
students_below_avg = find_students_below_average(students_data, group_avg)

print(f"\nСередній бал групи: {group_avg:.2f}")

print(f"\nСтуденти з балом нижче середнього:")
if students_below_avg:
    for student, avg in students_below_avg.items():
        print(f"- {student}: {avg:.2f}")
else:
    print("Усі студенти мають оцінки не нижче середнього!")