import json  # модуль для json
import logging

logger = logging.getLogger(__name__)

FILE_JSON = "file.json"  # файл для сохранения заметок

# загружаем заметки из файла в начале
try:

    with open(FILE_JSON, "r") as f:
        notes = json.load(f)  # открываем файл и загружаем данные

except json.JSONDecodeError as e:
    logger.error("Ошибка чтения файла")

    notes = []

except Exception as e:
    logger.error("Ошибка при загрузке заметок")

    notes = []

except FileNotFoundError:  # ошибка, если файла нет
    logger.error("Файл не найден")

    notes = []  # создаём пустой список


def save_notes():  # создаём функцию, которая сохраняет все заметки

    try:
        with open(FILE_JSON, "w") as f:
            json.dump(notes, f)  # сохраняем список в файл
        logger.info("Заметки сохранены")
    except Exception as e:
        logger.error("Ошибка при сохранении")


def add_note():  # создаём функцию, которая добавляет новые заметки

    try:
        title = input("Введите заголовок заметки: ")  # пользователь вводит заголовок
        text = input("Введите текст заметки: ")  # пользователь вводит текст
        notes.append(
            {"title": title, "text": text}
        )  # добавляем заметку как словарь в список
        save_notes()  # сохраняем
        print("Заметка добавлена!")
        logger.info("Добавлена новая заметка")

    except Exception as e:
        logger.error("Ошибка добавления")


def show_notes():  # создём функцию, которая показывает заметки

    if not notes:  # если нет заметок
        print("Нет сохраненных заметок")  # выводим, что заметок нет
        logger.info("Просмотр заметки, список пуст")
        return  # выходим из функции

    print("Ваши заметки:")

    for i, note in enumerate(notes, 1):  # нумеруем заметки
        print(f"{i}. {note['title']}")  # выводим номер и заголовок заметки
        print(note["text"])  # выводим текст заметки


def main():  # создём функцию, которая будет основным меню

    logger.info("Приложение запущенно")

    while True:  # бесконечный цикл
        print("Менеджер заметок")
        print("1. Добавить заметку")
        print("2. Показать заметки")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":  # если пользователь выбирает 1, добавляем заметку
            add_note()
        elif choice == "2":  # если пользователь выбирает 2, показываем заметки
            show_notes()
        elif choice == "3":  # если пользователь выбирает 3, выходим из приложения
            logger.info("Завершение работы")
            print("Выход из приложения")
            break
        else:  # иначе некорректный ввод
            logger.warning("Некорректный выбор")
            print("Некорректный ввод")


if __name__ == "__main__":  # запускаем главную функцию

    try:
        main()
    except Exception as e:
        logger.critical("Критическая ошибка")
        print("Критическая ошибка")
