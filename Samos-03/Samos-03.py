# Самостійна робота 3
def input_positive_int(entity):
    while True:
        try:
            input_qty = int(input(f"Введіть кількість {entity}: "))
            if input_qty <= 0:
                print(f"Кількість {entity} має бути більше 0!")
            else:
                break
        except ValueError:
            print("Помилка! Введіть ціле число")

    return input_qty

def input_books_qty():
    qty_books = input_positive_int("книг")
    return qty_books

def input_book_name():
    while True:
        book_name = input("Введіть назву книги: ").strip()
        if book_name:
            break
        else:
            print("Назва не може бути порожньою!")
    return book_name

def input_book_author():
    while True:
        book_author = input("Введіть автора: ").strip()
        if book_author:
            break
        else:
            print("Автор не може бути порожнім!")
    return book_author

def input_book_pages_qty():
    qty_pages = input_positive_int("сторінок")
    return qty_pages

def calculate_average_pages(books_dict):
    total_sum = 0
    total_count = 0

    for book_data in books_dict.values():
        total_sum += book_data["сторінок"]
        total_count += 1

    try:
        avg_qty = total_sum / total_count
    except ZeroDivisionError as e:
        print("Помилка в підрахунку середньої кількості сторінок", e)

    if avg_qty.is_integer(): return int(avg_qty)
    else: return round(avg_qty, 2)

def print_books_less_pages(books_dict, target_pages):
    print(f"\nКниги, що мають менше, ніж {target_pages} сторінок: ")
    for title, book_data in books_dict.items():
        if book_data["сторінок"] < target_pages:
            print(title, book_data)

def input_library():
    books_qty = input_books_qty()
    books = {}

    for book in range(books_qty):
        while True:
            in_title = input_book_name()
            if in_title in books:
                print("Книга з такою назвою вже є!")
            else:
                title = in_title
                break

        author = input_book_author()
        pages = input_book_pages_qty()

        books[title] = {
            "автор": author,
            "сторінок": pages
        }

    return books

def print_library(libra):
    print("\nКниги бібліотеки:")
    for title, book_data in libra.items():
        print(title, book_data)

books = input_library()

print_library(books)

avg_pages = calculate_average_pages(books)

print("\nСередня кількість сторінок:", avg_pages)

print_books_less_pages(books, avg_pages)