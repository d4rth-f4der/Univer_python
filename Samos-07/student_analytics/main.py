import json
from cli.args import parse_arguments
from reader.file_reader import read_csv_data
from parser.student_parser import get_students_list
from analysis.statistics import (
    calculate_student_averages,
    calculate_group_averages,
    get_students_above_group_average
)
from analysis.containers import create_group_dictionary, get_honors_groups
from reporting.charts import plot_group_average_scores, plot_subject_grade_distribution

def main():
    args = parse_arguments()

    all_students, subject_names = get_students_list(args.file, read_csv_data)

    if not all_students:
        print("Unable to get students data. End of execution")
        return

    students_to_analyze = all_students
    if args.group:
        students_to_analyze = [s for s in all_students if s["group"] == args.group]
        if not students_to_analyze:
            print(f"Students of group {args.group} not found")

    students_with_avg = calculate_student_averages(students_to_analyze)

    all_students_with_avg = calculate_student_averages(list(all_students))
    overall_group_averages = calculate_group_averages(all_students_with_avg)

    if args.group and args.group in overall_group_averages:
        display_group_averages = {args.group: overall_group_averages[args.group]}
    elif not args.group:
        display_group_averages = overall_group_averages
    else:
        display_group_averages = {}

    students_above_avg_in_their_group = get_students_above_group_average(students_with_avg, overall_group_averages)
    group_student_dict = create_group_dictionary(students_to_analyze)
    honors_groups_set = get_honors_groups(students_to_analyze)

    print("\n--- Analysis of students success ---")
    if args.group:
        print(f"Analysis for group: {args.group}")

    print("\nAverage students marks:")
    if students_with_avg:
        for student in students_with_avg:
            print(f"  {student['name']} ({student['group']}): {student.get('average_grade', 'N/A'):.2f}")
    else:
        print("  No students to display marks.")

    print("\nAverage marks by groups (to display on graph):")
    if display_group_averages:
        for group, avg in display_group_averages.items():
            print(f"  Group {group}: {avg:.2f}")
    else:
        print("  No data of average marks by groups for display.")

    print("\nStudents with higher than average marks in their group:")
    if students_above_avg_in_their_group:
        for name in students_above_avg_in_their_group:
            print(f"  {name}")
    else:
        print("  No such students(or no data).")

    print("\nDictionary {group: students list}:")
    if group_student_dict:
        for group, names in group_student_dict.items():
            print(f"  Group {group}: {', '.join(names)}")
    else:
        print("  Group dictionary is empty.")

    print("\nGroups with best students (all marks >= 90):")
    if honors_groups_set:
        print(f"  {', '.join(sorted(list(honors_groups_set)))}")
    else:
        print("  No groups with best students.")

    results_for_export = {
        "analyzed_group_filter": args.group if args.group else "All",
        "student_averages": [{s['name']: s.get('average_grade')} for s in students_with_avg if 'average_grade' in s],
        "group_averages_for_display": display_group_averages,
        "overall_group_averages": overall_group_averages,
        "students_above_their_group_average": students_above_avg_in_their_group,
        "group_to_students_dictionary": group_student_dict,
        "honors_groups": sorted(list(honors_groups_set))
    }
    if args.export:
        try:
            with open(args.export, 'w', encoding='utf-8') as f:
                json.dump(results_for_export, f, ensure_ascii=False, indent=4)
            print(f"\nAnalysis results written to {args.export}")
        except IOError:
            print(f"Error: couldn't write results to file {args.export}")
        except Exception as e:
            print(f"Unexpected error while export to JSON: {e}")

    if display_group_averages:
        plot_group_average_scores(display_group_averages)
    else:
        print("\nNo data for columns diagram of average marks by groups")

    if students_to_analyze and subject_names:
        plot_subject_grade_distribution(students_to_analyze, subject_names)
    else:
        print("\nNo data for boxplot of marks distribution")


if __name__ == "__main__":
    # Перед запуском убедитесь, что у вас установлены необходимые библиотеки:
    # pip install numpy matplotlib
    main()