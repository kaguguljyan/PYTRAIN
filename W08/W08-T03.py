# импортируем нужные инструменты из библиотеки SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()  # создаём базовый класс для таблицы


class User(Base):  # создаём класс User, который представляет таблицу в бд
    __tablename__ = "users"  # указываем имя таблицы в бд
    # создаём колонки в таблице, где
    id = Column(Integer, primary_key=True)  # id- главный ключ
    name = Column(String)  # name- строка с именем
    age = Column(Integer)  # age- число


engine = create_engine("sqlite:///users.db")  # подключаемся к бд SQLite
Base.metadata.create_all(engine)  # создаём таблицу users

Session = sessionmaker(bind=engine)  # создаём сессии
session = Session()  # открываем сессию

session.commit()  # сохраняем изменмения

users = session.query(User).all()  # выводим каждого пользователя
for user in users:
    print(f"{user.id}, {user.name}, {user.age}")

session.close()  # закрываем сессию
