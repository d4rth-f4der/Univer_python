import sys

print("Програма почала читати ввод:")
for line in sys.stdin:
    processed_line = line.strip()
    print(f"Прочитано: {processed_line}")

print("Програма завершила читати ввод.")