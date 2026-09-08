from collections.abc import Callable
from typing import Self


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str
        self.author: str
        self.year: int

        self.change_title(title)
        self.change_author(author)
        self.change_year(year)
        self.is_read = "не прочитано"

    def __str__(self) -> str:
        return f"название: {self.title}, автор: {self.author}, год: {self.year}, статус: {self.is_read}"

    def __repr__(self) -> str:
        return f"{self.title} - {self.author} {self.year} {self.is_read}"

    def mark_as_read(self) -> None:
        self.is_read = "прочитано"

    # noinspection PyAttributeOutsideInit
    def change_title(self, new_title: str) -> None:
        if new_title == '':
            raise ValueError("Ошибка! Название книги не может быть пустым!")

        self.title = new_title

    # noinspection PyAttributeOutsideInit
    def change_author(self, new_author: str) -> None:
        if new_author == '':
            raise ValueError("Ошибка! Имя автора не может быть пустым!")

        self.author = new_author

    # noinspection PyAttributeOutsideInit
    def change_year(self, new_year: int) -> None:
        if not (0 < new_year <= 2026):
            raise ValueError("Ошибка! Год должен состоять только из цифр от 0 до 2026!")

        self.year = new_year

    def change_book(self, field_choice: str, new_value: str | int) -> None:
        actions_dict = {
            'title': lambda: self.change_title(new_value),
            'author': lambda: self.change_author(new_value),
            'year': lambda: self.change_year(new_value)
        }
        actions_dict[field_choice]()


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str, author: str) -> int | None:
        for i, book in enumerate(self.books):
            if book.title == title and book.author == author:
                return i
        return None

    def delete_book(self, book: Book) -> None:
        self.books.remove(book)

    def get_book(self, index: int) -> Book:
        book = self.books[index]
        return book

    def show_books(self) -> list[Book]:
        return self.books

    def get_filter_library(self, function: Callable[[Book], bool]) -> Self:
        filter_books = list(filter(function, self.books))
        filter_library = Library()
        filter_library.books = filter_books
        return filter_library
