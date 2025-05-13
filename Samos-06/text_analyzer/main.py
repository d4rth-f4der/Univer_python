# Точка входу — обробка командного рядка
import argparse
import sys
import os

from .parser import tokenizer
from .analysis import helpers
from .analysis import word_stats
from .analysis import digit_stats
from .output import printer
from .output import json_printer

def read_text_from_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        print(f"Помилка: Файл не знайдено: {filepath}", file=sys.stderr)    # stderr - стандартний потік помилок
        sys.exit(1)         # Завершення програми з кодом помилки

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Помилка читання файлу {filepath}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Текстовий аналізатор - аналізує текст з аргументу або файлу.",
        epilog="Приклади використання: python -m text_analyzer.main \"Привіт світ!\" або"
               "python -m text_analyzer.main -f data/test.txt"
    )

    group = parser.add_mutually_exclusive_group(required=True) # група аргументів, які виключають один одного.

    group.add_argument(
        "text",
        nargs="?",      # Дозволяє передати 0 або 1 позиційний аргумент
        help="Текст для аналізу, якщо не використовується прапор -f"
    )

    group.add_argument(
        "-f", "--file",
        metavar="FILE",
        help="Шлях до текстового файлу для аналізу"
    )

    output_format_group = parser.add_mutually_exclusive_group()
    output_format_group.add_argument(
        "--json",
        action="store_true",
        help="Вивести результат аналізу у форматі JSON замість стандартної таблиці."
    )

    args = parser.parse_args()

    input_text = None

    if args.text:
        input_text = args.text
        print("Отримано текст для аналізу з аргументу командного рядка.")
    elif args.file:
        input_text = read_text_from_file(args.file)
        print(f"Читаємо текст з файлу: {args.file}")

    if input_text is not None:
        print("\n--- Запуск аналізу тексту ---")

        print("Крок 1/4: Аналізуємо кількість речень...")
        sentences_qty = word_stats.count_sentences(input_text)

        print("Крок 2/4: Виконуємо токенізацію тексту...")
        tokens = tokenizer.tokenize(input_text)

        print("Крок 3/4: Аналізуємо статистику слів та чисел...")

        word_count = word_stats.count_words(tokens)
        words_len_3_count = word_stats.count_words_len(tokens, 3)
        unique_word_count = word_stats.count_unique_words(tokens)
        titlecase_word_count = word_stats.count_titlecase_words(tokens)
        digit_count = digit_stats.count_digits(tokens)
        alternations = digit_stats.alternation_count(tokens)

        analysis_results = {
            "sentence_count": sentences_qty,
            "word_count": word_count,
            "words_len_3": words_len_3_count,
            "unique_words": unique_word_count,
            "titlecase_words": titlecase_word_count,
            "digit_count": digit_count,
            "alternation_count": alternations
        }

        print("Крок 4/4: Форматуємо та виводимо звіт...")
        print("\n--- Вивод результатів ---")

        if args.json:
            print("Формат виводу: JSON")
            json_printer.print_json(analysis_results)
        else:
            print("Формат виводу: Таблиця")
            printer.print_report(analysis_results)


    else:
         print("Помилка: Не вдалося отримати текст для аналізу.", file=sys.stderr)
         sys.exit(1)

if __name__ == "__main__":
    main() # виклик, якщо файл main.py запущено безпосередньо