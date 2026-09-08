import menu
import storage


def main():
    library = storage.load_library()

    # Словарь дейстивий пользователя
    actions = menu.create_actions(library)

    menu.show_menu()
    user_choice = menu.get_user_choice()
    while user_choice != '0':
        menu.user_actions(user_choice, actions)
        menu.continue_message()
        menu.show_menu()
        user_choice = menu.get_user_choice()
    storage.save_library(library)


if __name__ == "__main__":
    main()
