# Практична 2 задача 2 - на функціях

def add_book(books_dict):
    while True:
        book_input = input("Назва та автор через кому(або 'stop'): ")
        if book_input.lower() == 'stop':
            break
        try:
            book, author = book_input.split(',',1)
            books_dict[book.strip()] = author.strip()
        except ValueError:
            print("Некоректний ввід, спробуйте ще раз.")
    return books_dict

def find_book_author(books_dict):
    book_to_find = input("Введіть назву книги для пошуку її автора: ")
    if book_to_find in books_dict:
        print(f"Автор книги '{book_to_find}': {books_dict[book_to_find]}")
    else:
        print("Книга не знайдена в базі даних")

def main():
    books = {}
    books = add_book(books)
    find_book_author(books)

main()