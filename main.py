import menu


def main():
    # Спискок для хранения всех книг(словарей)
    library = []

    # Словарь дейстивий пользователя
    actions = menu.create_actions(library)

    menu.show_menu()
    user_choice = menu.get_user_choice()
    while user_choice != '0':
        menu.user_actions(user_choice, actions)
        menu.continue_message()
        menu.show_menu()
        user_choice = menu.get_user_choice()


if __name__ == "__main__":
    main()
