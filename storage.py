import json


def save_library(library):
    with open('my_library.json', 'w', encoding='utf-8') as f:
        json.dump(library, f, indent=4, ensure_ascii=False)

    print("Ваша библиотека успешно сохранена в системе!")


def load_library():
    try:
        with open('my_library.json', 'r', encoding='utf-8') as f:
            library = json.load(f)
        print("Ваша библиотека успешно загружена!")

    except json.JSONDecodeError:
        library = []
        print("Ошибка при загрузки библиотеки!")
    except FileNotFoundError:
        library = []
        print("Файл с сохраненной библиотекой не найден!")
    return library
