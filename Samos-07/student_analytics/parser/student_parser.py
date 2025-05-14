def parse_student_data(row_data, subject_names):
    if len(row_data) < 2 + len(subject_names):
        print(f"Error: insufficient data in string: {row_data}. Excpected {2 + len(subject_names)} columns.")
        return None

    student_name = row_data[0]
    group = row_data[1]

    try:
        grades = [int(grade) for grade in row_data[2:2 + len(subject_names)]]
    except ValueError:
        print(f"Error: incorrect format for mark of student {student_name} in group {group}. String: {row_data}")
        return None

    return {"name": student_name, "group": group, "grades": grades}


def get_students_list(file_path, file_reader_func):
    students = []
    subject_names = []

    data_generator = file_reader_func(file_path)

    header = next(data_generator, None)
    if header is None or len(header) < 3:
        print("Error: unable to read header or incorrect header")
        return [], []

    subject_names = header[2:]

    for row in data_generator:
        if row is None:
            continue
        student_data = parse_student_data(row, subject_names)
        if student_data:
            students.append(student_data)

    if not students:
        print("Warning: students list empty after parsing")

    return students, subject_names