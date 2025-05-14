def create_group_dictionary(students):
    group_dict = {}
    for student in students:
        group = student["group"]
        if group not in group_dict:
            group_dict[group] = []
        group_dict[group].append(student["name"])
    return group_dict


def get_honors_groups(students):
    honors_groups = set()
    for student in students:
        if not student["grades"]:
            continue
        is_honors_student = all(grade >= 90 for grade in student["grades"])

        if is_honors_student:
            honors_groups.add(student["group"])
    return honors_groups