from FullTimeStudent import FullTimeStudent
from PartTimeStudent import PartTimeStudent

student1 = FullTimeStudent(name="Kolia", age=24, prac_score=910, prac_count=10, exam_scr=95, attend_pct=85)
student2 = FullTimeStudent("Vasia", 19, 930, 10, 99, 20)
student3 = PartTimeStudent("Sonia", 20, 156, 8,89)


university_students = [student1, student2, student3]

for student in university_students:
    student.display_info()
    print(f"""Ім'я: {student.name}
    Вік: {student.age}
    Середній бал за практичні: {student.avg_practice_score()}""")
    if isinstance(student, FullTimeStudent):
        print(f"Загальний бал: {student.total_score()}\n")
    elif isinstance(student, PartTimeStudent):
        print(f"Загальний бал (заочно): {student.total_score()}\n")