# Проверка книги перед созданием
def validation_book(title, author, year):
    while title == "":
        title = input('Название книги не может быть пустым, введите хотя бы один символ: ')
    # С цифрами разберусь потом
    while author == "":
        author = input('Имя автора не должно быть пустым. Введите автора книги заново: ')
    while not year.isdigit():
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    while not(0 < int(year) <= 2026):
        year = input('Год должен состоять только из цифр от 0 до 2026. Введите год издания книги заново: ')
    return title, author, year


# Функция для создания книги
def create_book():
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год издания книги: ')
    title, author, year = validation_book(title, author, year)
    book = dict(title=title, author=author, year=int(year))
    return book


# Функция для добавления книги в библиотеку
def add_book(book, library):
    if find_book(book["title"], book["author"], library) is not None:
        print("Эта книга уже есть в библиотеке!")
    else:
        library.append(book)
        print("Книга успешно добавлена в библиотеку!")


# Функция для добавления книги в библиотеку через меню
def menu_add_book(library):
    book = create_book()
    add_book(book, library)


# Функция поиска книги в библиотеке
def find_book(title, author, library):
    for i, book in enumerate(library):
        if book["title"] == title and book["author"] == author:
            return i
    return None


def menu_find_book(library):
    print("Поиск книг в библиотеке")
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    index = find_book(title, author, library)
    if index is not None:
        print(f"Книга найдена на позиции {index+1}!")
    else:
        print("Данная книга не существует!")


def show_menu():
    print("=============")
    print("1. Добавить книгу")
    print("2. Удалить книгу - в разработке")
    print("3. Показать библиотеку - в разработке")
    print("4. Найти книгу")
    print("0. Выход")
    print("=============")


def continue_message():
    input("Нажмите Enter для продолжения... ")


def get_user_choice():
    return input("Ваш выбор: ")


def user_actions(choice, actions):
    try:
        actions[choice]()
    except KeyError:
        print("Неизвестная команда!")


def log_out_of_system():
    print("Вы вышли из системы!")


def main():
    # Спискок для хранения всех книг(словарей)
    library = []

    # Словарь дейстивий пользователя
    actions = {
        '1': lambda: menu_add_book(library),
        '4': lambda: menu_find_book(library),
        '0': log_out_of_system
    }

    show_menu()
    user_choice = get_user_choice()
    while user_choice != '0':
        user_actions(user_choice, actions)
        continue_message()
        show_menu()
        user_choice = get_user_choice()


if __name__ == "__main__":
    main()

