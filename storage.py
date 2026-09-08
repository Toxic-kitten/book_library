from models import Library, Book
import json


def save_library(library: Library) -> None:
    with open('my_library.json', 'w', encoding='utf-8') as f:
        library_list = []
        for book in library.books:
            new_book = dict(title=book.title, author=book.author, year=book.year, is_read=book.is_read)
            library_list.append(new_book)
        json.dump(library_list, f, indent=4, ensure_ascii=False)

    print("Ваша библиотека успешно сохранена в системе!")


def load_library() -> Library:
    library = Library()
    try:
        with open('my_library.json', 'r', encoding='utf-8') as f:
            library_list = json.load(f)
            for book in library_list:
                object_book = Book(book["title"], book["author"], book["year"])
                object_book.is_read = book["is_read"]
                library.add_book(object_book)
        print("Ваша библиотека успешно загружена!")

    except json.JSONDecodeError:
        library.books = []
        print("Ошибка при загрузки библиотеки!")
    except FileNotFoundError:
        library.books = []
        print("Файл с сохраненной библиотекой не найден!")
    return library
