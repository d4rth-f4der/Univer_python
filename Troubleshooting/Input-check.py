import sys

# Виводимо кодування стандартного виводу
print(f"sys.stdout.encoding: {sys.stdout.encoding}")
# Виводимо кодування стандартного вводу
print(f"sys.stdin.encoding: {sys.stdin.encoding}")

print("Програма спробує прочитати рядок зі стандартного вводу...")

try:
    # Читаємо один рядок зі стандартного вводу
    # Python використає кодування sys.stdin.encoding для його декодування
    line = sys.stdin.readline()

    if not line:
        print("Прочитано порожній рядок або досягнуто EOF одразу.")
    else:
        # Виводимо прочитаний рядок та його представлення після декодування
        print(f"Прочитано (до декодування): {line!r}") # Вивід рядка "як є" з escape-послідовностями
        print(f"Декодовано (з sys.stdin.encoding): '{line.strip()}'") # Вивід після декодування та видалення пробілів

except EOFError:
    print("Досягнуто кінця вводу (EOF).")
except Exception as e:
    print(f"Виникла помилка при читанні зі стандартного вводу: {e}")

print("Програма завершила роботу.")