# импортируем нужные инструменты из библиотеки SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine("sqlite:///notes.db") # подключаемся к бд SQLite
Base = declarative_base() # создаём базовый класс для таблицы
Session = sessionmaker(bind=engine) # создаём сессии


class Note(Base): # создаём класс Note, который представляет таблицу в бд
    __tablename__ = "notes" # указываем имя таблицы в бд
    id = Column(Integer, primary_key=True) # id- главный ключ
    title = Column(String(50)) # title- строчка с заголовком
    text = Column(Text) # text- текст 
    created_at = Column(DateTime, default=datetime.now) # created_at- дата добавления


Base.metadata.create_all(engine) # создаём таблицу users


def load_notes(): # загружаем все заметки из бд
    """Загружает заметки из файла."""
    session = Session() # соединяемся с бд
    notes = session.query(Note).all() # получаем все заметки из таблицы
    session.close() # закрываем соединение
    return notes # возвращаем список заметок


def save_notes(note=None):  # сохраняем заметку
    """Сохраняет заметки в файл."""
    if note: # если заметка передана, соединяем с бд
        session = Session()
        try:
            session.add(note) # добавляем заметку
            session.commit() # сохраняем изменения
        finally:
            session.close()


def add_note(title, text):  # добавляем заметку
    """Добавляет новую заметку."""
    session = Session()
    note = Note(title=title, text=text) # создаём объект заметки с переданным заголовком и текстом
    session.add(note)
    session.commit()
    session.close()
    print("Заметка добавлена")


def show_notes():  # показываем все заметки
    """Показывает заметки."""
    session = Session()
    notes = session.query(Note).all() # получаем все заметки из таблицы
    session.close()
    if not notes: 
        print("Заметок нет")
        return 
    print("Менеджер заметок")
    for note in notes: 
        print(f"{note.id}, {note.title}")
        print(note.text)
        print(f"{note.created_at}")


def main():
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
            add_note(title, text)
            print("Заметка добавлена!")
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("Выход из приложения")
            break
        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
