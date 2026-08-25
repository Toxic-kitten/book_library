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
    book = dict(title=title, author=author, year=int(year), is_read="не прочитана")
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


# Функция для вывода всей библиотеки
def show_library(library):
    print("Ваша библиотека")
    print('1. Показать только прочитанные книги')
    print('2. Показать только не прочитанные книги')
    print("3. Показать все книги")
    lib_actions = {
        '1': lambda: make_filter_books_list(is_read, library),
        '2': lambda: make_filter_books_list(is_not_read, library),
        '3': lambda: library
    }
    user_choice = get_user_choice()
    choice_books = library_actions(user_choice, lib_actions)
    if choice_books is None:
        print("Неизвестная команда!")
    elif not choice_books:
        print("Список пуст")
    else:
        show_books(choice_books)


def library_actions(choice, actions):
    try:
        return actions[choice]()
    except KeyError:
        return None


def make_filter_books_list(function, library):
    filter_books = list(filter(function, library))
    return filter_books


def show_books(library):
    for num, book in enumerate(library):
        print(f'{num + 1}) {book["title"]}, {book["author"]}, {book["year"]}, статус: {book["is_read"]}')


def is_read(book):
    return book["is_read"] == 'прочитано'


def is_not_read(book):
    return not is_read(book)


def mark_as_read(book):
    book['is_read'] = "прочитано"


def menu_mark_as_read(library):
    if len(library) != 0:
        print("Выберите книгу которую вы прочитали:")
        show_books(library)
        user_choice = get_user_choice()
        try:
            book = library[int(user_choice) - 1]
            if book['is_read'] != "прочитано":
                mark_as_read(book)
                print(f"Книга {book['title']} отмечена как прочитанная!")
            else:
                print(f"Книга {book['title']} уже отмечена как прочитанная!")
        except IndexError:
            print("Неизвестный номер книги! Попробуйте ввести номер еще раз.")
        except ValueError:
            print("Вы ввели текст, а не число! Попробуйте ввести номер еще раз.")
    else:
        print("Ваша библиотека пуста, сначала добавьте хотя бы одну книгу!")


def menu_delete_book(library):
    if len(library) != 0:
        print("Выберите номер книги которую вы хотите удалить:")
        show_library(library)
        user_choice = get_user_choice()
        try:
            index = int(user_choice) - 1
            book = library[index]
            delete_book(index, library)
            print(f"Книга {book['title']} успешно удалена!")
        except IndexError:
            print("Неизвестный номер книги! Попробуйте ввести номер еще раз.")
        except ValueError:
            print("Вы ввели текст, а не число! Попробуйте ввести номер еще раз.")
    else:
        print("Ваша библиотека пуста, сначала добавьте хотя бы одну книгу!")


def delete_book(index, library):
    del library[index]


def show_menu():
    print("=============")
    print("1. Добавить книгу")
    print("2. Отметить книгу как прочитанную")
    print("3. Показать библиотеку")
    print("4. Найти книгу")
    print("5. Удалить книгу")
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
        '2': lambda: menu_mark_as_read(library),
        '3': lambda: show_library(library),
        '4': lambda: menu_find_book(library),
        '5': lambda: menu_delete_book(library),
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
