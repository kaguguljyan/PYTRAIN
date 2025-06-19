from fastapi import FastAPI  # импорт библиотеки для FastAPI
from pydantic import BaseModel  # импорт библиотеки для BaseModel
import json  # для работы с файлами json
import logging
import time
import requests

app = FastAPI()  # создаем экземпляр приложения FastAPI

# настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

FILE_JSON = "file.json"


# определяем структуру заметки (pydantic)
class Note(BaseModel):
    title: str  # строка с заголовком
    text: str  # строка с текстом


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


def create_id():
    # Используем текущее время в секундах как ID
    return str(int(time.time()))


# эндпоинт для получения всех заметок
@app.get("/notes")
async def get_notes():
    try:
        return {
            "notes": load_notes()
        }  # загруэаем заметки из файла и возвращаем их в формате json
    except Exception as e:
        logger.error(f"Ошибка при получении заметок: {e}")
        return {"error": "Заметки не загрузились"}


@app.get("/")
def get_root():
    return {"message": "Менеджер заметок!"}


# эндпоинт для получения одной заметки по ID
@app.get("/note/{note_id}")
def get_note(note_id: str):  # note_id получаем из URL
    try:
        notes = load_notes()  # загружаем все заметки
        for note in notes:  # ищем заметку с нужным ID
            if note["id"] == note_id:
                return note
        return {"error": "Заметка не найдена"}
    except Exception as e:
        logger.error(f"Ошибка при получении заметки: {e}")
        return {"error": "Заметка не получена"}


# эндпоинт для создания новой заметки
@app.post("/notes")
def add_note(note: Note):  # получаем данные заметки из тела запроса
    try:
        notes = load_notes()  # загружаем заметки
        new_note = {
            "id": create_id(),
            "title": note.title,
            "text": note.text,
        }  # создаем новую заметку с ID (генерируем уникальный ID, берем заголовок из запроса, берем текст из запроса)
        notes.append(new_note)  # добавляем новую заметку в список
        save_notes(notes)  # сохраняем обновленный список в файл
        return {
            "message": "Заметка добавлена",
            "note": new_note,
        }  # возвращаем сообщение и созданную заметку
    except Exception as e:
        logger.error(f"Ошибка при создании заметки: {e}")
        return {"error": "Заметка не создана"}


# эндпоинт для обновления заметки
@app.put("/notes/{note_id}")
def update_note(note_id: str, note: Note):
    try:
        notes = load_notes()  # загружаем текущие заметки
        for i, existing_note in enumerate(
            notes
        ):  # перебираем заметки чтобы найти нужную
            if existing_note["id"] == note_id:
                update_note = {
                    "id": note_id,
                    "title": note.title,
                    "text": note.text,
                }  # создаем обновленную версию заметки (ID остается прежним, новые данные из запроса)
                notes[i] = update_note  # заменяем старую заметку на обновленную
                save_notes(notes)  # сохраняем изменения
                return {"message": "Заметка обновлена", "note": update_note}
        return {"error": "Замтека не найдена"}
    except Exception as e:
        logger.error(f"Ошибка при обновлении заметки: {e}")
        return {"error": "Заметка не обновлена"}


# эндпоинт для удаления заметки
@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    try:
        notes = load_notes()  # загружаем текущие заметки
        new_notes = [
            note for note in notes if note["id"] != note_id
        ]  # создаем новый список без удаляемой заметки
        if len(new_notes) == len(
            notes
        ):  # если длина спика не изменилась, значит заметка не найдена
            return {"error": "Заметка не найдена"}
        save_notes(new_notes)  # сохраняем новый список
        return {"message": "Заметка удалена"}
    except Exception as e:
        logger.error(f"Ошибка при удалении заметки: {e}")
        return {"error": "Заметка не удалена"}


def check_api():
    try:
        r = requests.get(
            "http://127.0.0.1:8000/docs", timeout=2
        )  # отправляем GET запрос к url
        r.raise_for_status()  # проверяем, что запрос завершился успешно
        return True  # если запрос выполнен успешно, возвращаем True
    except (
        requests.exceptions.Timeout
    ):  # ловим исключение, если запрос превысил 2 секунды
        logger.error("Timeout")  # сообщение об ошибке
        return False
    except (
        requests.exceptions.ConnectionError
    ):  # ловим исключение, если не удалось установить соединение
        logger.error("Подключение к API не удалось")
        return False
    except (
        requests.exceptions.RequestException
    ) as e:  # ловим исключения, связанные с запросами
        logger.error(f"Ошибка при проверке API: {e}")
        return False


# запускаем
if __name__ == "__main__":
    import uvicorn

    logger.info(
        "Сервера API запускаются"
    )  # записываем сообщение с информацией о запуске сервера
    uvicorn.run(
        app, host="127.0.0.1", port=8000
    )  # запускаем сервер на localhost с port 8000
