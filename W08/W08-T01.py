import sqlite3  # импортируем модуль sqlite3 для работы с бд

con = sqlite3.connect("RUDN.db")  # подключаемся к бд
cur = con.cursor()  # создём курсор для выполнения sql запросов

cur.execute(
    "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
)  # создание таблицы students с тремя столбцами id, name, age
cur.execute(
    """INSERT INTO students (id, name, age) VALUES (1, 'Ксения', 22), (2, 'Лера', 23)"""
)  # вставляем записи в таблицу
con.commit()  # сохраняем изменения в бд
con.close()  # закрываем соединение с бд