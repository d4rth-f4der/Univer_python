import sys
import math

def print_help():
    print("Використання: python назва_скрипта.py [команда]")
    print("Доступні команди:")
    print("  pi    - Вивести число Pi з 3-4 знаками після крапки.")
    print("  e     - Вивести число Ейлера (e) з 6 знаками після крапки.")
    print("  help  - Вивести цю довідку.")

def main():
    if len(sys.argv) != 2:
        print("Помилка: Невірна кількість аргументів.")
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "pi":
        print(f"Число Pi: {math.pi:.4f}")
    elif command == "e":
        print(f"Число Ейлера (e): {math.e:.6f}")
    elif command == "help":
        print_help()
    else:
        print(f"Помилка: Незрозуміла команда '{sys.argv[1]}'.")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()