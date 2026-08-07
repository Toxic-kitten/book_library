# Проверка книги перед созданием
def validation_book(name, author, year):
    while name == "":
        name = input('Название книги не может быть пустым, введите хотя бы один символ: ')
    # С цифрами разберусь потом
    while author == "":
        author = input('Имя автора не должно быть пустым. Введите автора книги заново: ')
    while not year.isdigit():
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    while not(0 < int(year) <= 2026):
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    return dict(name=name, author=author, year=int(year))


# Функция для создания книги
def create_book():
    name = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год издания книги: ')
    book = validation_book(name, author, year)
    return book


# Функция для добавления книги в библиотеку
def add_book(book, library):
    library.append(book)
    print("Книга успешно добавлена в библиотеку!")


def find_book(library):
    print("Поиск книг в библиотеке")
    name = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    index = -1
    for i in range(len(library)):
        if library[i]["name"] == name and library[i]["author"] == author:
            print(f"Книга найдена! Ее номер в библиотеке: {i+1}")
            index = i
            break
        else:
            print("Книга не найдена!")
    return index


def main():
    # Спискок для хранения всех книг(словарей)
    library = []

    book1 = create_book()
    add_book(book1, library)
    print(library)
    print(find_book(library))


if __name__ == "__main__":
    main()

