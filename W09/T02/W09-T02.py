import json
import logging

# настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

FILE_JSON = "file.json"

def load_notes():
    """Загружает заметки из файла."""
    try:
        with open(FILE_JSON, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("Файл не найден, создается новый список заметок.")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка чтения файла, данные повреждены.")
        return []
    except Exception as e:
        logger.error(f"Ошибка при загрузке заметок: {e}")
        return []

def save_notes(notes):  # изменено на принятие notes как аргумента
    """Сохраняет заметки в файл."""
    try:
        with open(FILE_JSON, "w") as f:
            json.dump(notes, f)
        logger.info("Заметки сохранены")
    except Exception as e:
        logger.error(f"Ошибка при сохранении заметок: {e}")

def add_note(notes, title, text):  # изменено на принятие notes как аргумента
    """Добавляет новую заметку."""
    notes.append({"title": title, "text": text})
    save_notes(notes)
    logger.info("Добавлена новая заметка")

def show_notes(notes):  # изменено на принятие notes как аргумента
    """Показывает заметки."""
    if not notes:
        print("Нет сохраненных заметок")
        logger.info("Просмотр заметки, список пуст")
        return

    print("Ваши заметки:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}")
        print(note["text"])

def main():
    logger.info("Приложение запущено")
    notes = load_notes()  # загружаем заметки при запуске

    while True:
        print("Менеджер заметок")
        print("1. Добавить заметку")
        print("2. Показать заметки")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            text = input("Введите текст заметки: ")
            add_note(notes, title, text)
            print("Заметка добавлена!")
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            logger.info("Завершение работы")
            print("Выход из приложения")
            break
        else:
            logger.warning("Некорректный выбор")
            print("Некорректный ввод")

if __name__ == "__main__":
    main()