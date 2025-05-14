import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Console app for analysing of students marks")
    parser.add_argument("--file", type=str, required=True,
                        help="Path to CSV-file with marks (eg, data/grades.csv).")
    parser.add_argument("--group", type=str,
                        help="Filter by group to show statistics (например, KN-21).")
    parser.add_argument("--export", type=str,
                        help="Path to JSON-file for exporting the analysis results")

    return parser.parse_args()