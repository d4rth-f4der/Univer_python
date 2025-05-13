# Форматований вивод результатів

def print_report(stats: dict):
    col1_width = 27
    col2_width = 8

    separator_line = "+" + "-" * (col1_width + 2) + "+" + "-" * (col2_width + 2) + "+"

    header_line = f"| {'Показник':<{col1_width}} | {'Значення':<{col2_width}} |"

    print(separator_line)
    print(header_line)
    print(separator_line)

    for label, value in stats.items():
        value_str = str(value)
        print(f"| {str(label):<{col1_width}} | {value_str:>{col2_width}} |")

    print(separator_line)