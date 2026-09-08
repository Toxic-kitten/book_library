from models import Library, Book


def continue_message():
    input("Нажмите Enter для продолжения... ")


def log_out_of_system():
    print("Вы вышли из системы!")


def get_user_choice():
    return input("Ваш выбор: ")


def user_actions(choice, actions_dict):
    try:
        actions_dict[choice]()
    except KeyError:
        print("Неизвестная команда!")


def create_actions(library):
    actions_dict = {
        '1': lambda: menu_add_book(library),
        '2': lambda: menu_mark_as_read(library),
        '3': lambda: menu_edit_book(library),
        '4': lambda: menu_delete_book(library),
        '5': lambda: menu_find_book(library),
        '6': lambda: menu_show_library(library),
        '0': log_out_of_system
    }
    return actions_dict


def show_menu():
    print("=============")
    print("1. Добавить книгу")
    print("2. Отметить книгу как прочитанную")
    print("3. Изменить книгу")
    print("4. Удалить книгу")
    print("5. Найти книгу")
    print("6. Показать библиотеку")
    print("0. Выход")
    print("=============")


def menu_add_book(library: Library):
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    try:
        year = int(input('Введите год издания книги: '))
    except ValueError:
        return print("Ошибка! Вы ввели текст при добавления книги")
    try:
        book = Book(title, author, year)
    except ValueError as error:
        return print(error)
    library.add_book(book)


def menu_find_book(library: Library):
    print("Поиск книг в библиотеке")
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    index = library.find_book(title, author)
    if index is not None:
        print(f"Книга найдена на позиции {index+1}!")
    else:
        print("Данная книга не существует!")


# Функция для вывода всей библиотеки
def menu_show_library(library):
    print("Ваша библиотека")
    print('1. Показать только прочитанные книги')
    print('2. Показать только не прочитанные книги')
    print("3. Показать все книги")
    lib_actions = {
        '1': lambda: library.get_filter_library(is_read),
        '2': lambda: library.get_filter_library(is_not_read),
        '3': lambda: library
    }
    user_choice = get_user_choice()
    choice_books = library_actions(user_choice, lib_actions)
    if choice_books is None:
        print("Неизвестная команда!")
    elif not choice_books.books:
        print("Список пуст")
    else:
        menu_show_books(choice_books)


def library_actions(choice, lib_actions):
    try:
        return lib_actions[choice]()
    except KeyError:
        return None


def is_read(book):
    return book.is_read == 'прочитано'


def is_not_read(book):
    return not is_read(book)


def menu_show_books(library: Library):
    books = library.show_books()
    for num, book in enumerate(books):
        print(f'{num + 1}) {book.title}, {book.author}, {book.year}, статус: {book.is_read}')


def menu_mark_as_read(library: Library):
    if not library.books:
        return print("Ваша библиотека пуста, сначала добавьте хотя бы одну книгу!")

    print("Выберите номер книги которую вы хотите изменить:")
    menu_show_books(library)

    user_choice = get_user_choice()
    try:
        index = int(user_choice) - 1
        book = library.get_book(index)
        print(f'Книга: {book.title}, {book.author}, {book.year}, статус: {book.is_read}')

        if book.is_read != "прочитано":
            book.mark_as_read()
            print(f"Книга {book.title} отмечена как прочитанная!")
        else:
            print(f"Книга {book.title} уже отмечена как прочитанная!")
    except IndexError:
        print("Неизвестный номер книги! Попробуйте ввести номер еще раз.")
    except ValueError:
        print("Вы ввели текст, а не число! Попробуйте ввести номер еще раз.")


def menu_delete_book(library):
    if not library.books:
        return print("Ваша библиотека пуста, сначала добавьте хотя бы одну книгу!")

    print("Выберите номер книги которую вы хотите удалить:")
    menu_show_books(library)
    user_choice = get_user_choice()
    try:
        index = int(user_choice) - 1
        book = library.get_book(index)
        library.delete_book(book)
        print(f"Книга {book.title} успешно удалена!")
    except IndexError:
        print("Неизвестный номер книги! Попробуйте ввести номер еще раз.")
    except ValueError:
        print("Вы ввели текст, а не число! Попробуйте ввести номер еще раз.")


def menu_edit_book(library: Library):
    if not library.books:
        return print("Ваша библиотека пуста, сначала добавьте хотя бы одну книгу!")

    print("Выберите номер книги которую вы хотите изменить:")
    menu_show_books(library)

    user_choice = get_user_choice()
    try:
        index = int(user_choice) - 1
        book = library.get_book(index)
        print(f'Книга: {book.title}, {book.author}, {book.year}, статус: {book.is_read}')

        print("Выберите что вы конкретно хотите изменить:")
        print("Напишите название поля(title/author/year):")
        fields = ['title', 'author', 'year']
        field_choice = get_user_choice()
        field_choice = user_choice_validation(field_choice, fields)

        print("Напишите новое значение поля:")
        new_value = get_user_choice()
        if field_choice == 'year':
            new_value = int(new_value)
        book.change_book(field_choice, new_value)
        print("Книга успешно изменена!")
    except IndexError:
        print("Неизвестный номер книги! Попробуйте ввести номер еще раз.")
    except ValueError:
        print("Вы ввели текст, а не число! Попробуйте ввести номер еще раз.")


def user_choice_validation(user_choice, available_options):
    while user_choice not in available_options:
        print("Выберете один доступных вариантов:", *available_options)
        user_choice = input("Ваш выбор: ")
    return user_choice
