import matplotlib.pyplot as plt
import numpy as np

def plot_group_average_scores(group_averages):
    if not group_averages:
        print("No data for plotting average marks graphics by groups")
        return

    groups = list(group_averages.keys())
    averages = list(group_averages.values())

    plt.figure(figsize=(10, 6))
    plt.bar(groups, averages, color='skyblue')
    plt.xlabel("Group")
    plt.ylabel("Average mark")
    plt.title("Average mark by groups")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()


def plot_subject_grade_distribution(students, subject_names):
    if not students:
        print("No students ddata for plotting marks distribution graphics")
        return
    if not subject_names:
        print("No subject names to plot graphics")
        return

    num_subjects = len(subject_names)
    grades_by_subject = [[] for _ in range(num_subjects)]

    for student in students:
        if len(student["grades"]) == num_subjects:
            for i in range(num_subjects):
                grades_by_subject[i].append(student["grades"][i])

    if not any(grades_by_subject):
        print("Insufficient marks data to build boxplot.")
        return

    plt.figure(figsize=(12, 7))
    filtered_grades_by_subject = [grades for grades in grades_by_subject if grades]
    filtered_subject_names = [name for i, name in enumerate(subject_names) if grades_by_subject[i]]

    if not filtered_grades_by_subject:
        print("No data to build boxplot after filtering of empty subjects")
        return

    plt.boxplot(filtered_grades_by_subject, labels=filtered_subject_names, patch_artist=True)
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Marks distribution by subjects")
    plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()