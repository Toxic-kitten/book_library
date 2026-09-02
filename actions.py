# Проверка книги перед созданием
def validation_book(title, author, year):
    while title == "":
        title = input('Название книги не может быть пустым, введите хотя бы один символ: ')
    # С цифрами разберусь потом
    while author == "":
        author = input('Имя автора не должно быть пустым. Введите автора книги заново: ')
    while not year.isdigit():
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    while not (0 < int(year) <= 2026):
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    return title, author, year


# Функция для создания книги
def create_book():
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год издания книги: ')
    title, author, year = validation_book(title, author, year)
    book = dict(title=title, author=author, year=int(year), is_read="не прочитана")
    return book


# Функция для добавления книги в библиотеку
def add_book(book, library):
    if find_book(book["title"], book["author"], library) is not None:
        print("Эта книга уже есть в библиотеке!")
    else:
        library.append(book)
        print("Книга успешно добавлена в библиотеку!")


# Функция поиска книги в библиотеке
def find_book(title, author, library):
    for i, book in enumerate(library):
        if book["title"] == title and book["author"] == author:
            return i
    return None


# Функция удаления книги из библиотеки
def delete_book(index, library):
    del library[index]


# Отметить книгу как прочитанную
def mark_as_read(book):
    book['is_read'] = "прочитано"
