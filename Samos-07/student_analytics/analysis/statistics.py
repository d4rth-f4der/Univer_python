import numpy as np

def calculate_student_averages(students):
    for student in students:
        if student["grades"]:
            student["average_grade"] = np.mean(student["grades"])
        else:
            student["average_grade"] = 0.0
    return students


def calculate_group_averages(students):
    group_grades_all = {}
    for student in students:
        group = student["group"]
        if group not in group_grades_all:
            group_grades_all[group] = []
        group_grades_all[group].extend(student["grades"])

    group_averages = {}
    for group, all_grades_list in group_grades_all.items():
        if all_grades_list:
            group_averages[group] = np.mean(all_grades_list)
        else:
            group_averages[group] = 0.0
    return group_averages


def get_students_above_group_average(students, group_averages):
    students_above_average = []
    for student in students:
        group_avg = group_averages.get(student["group"])
        if group_avg is not None and student.get("average_grade", 0.0) > group_avg:
            students_above_average.append(student["name"])
    return students_above_average