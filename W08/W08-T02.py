import sqlite3

con = sqlite3.connect("users.db")  # подключаемся к бд
cur = con.cursor()  # создём курсор для выполнения sql запросов

cur.execute(
    "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
)  # создание таблицы users с тремя столбцами id, name, age
cur.execute(
    """INSERT INTO users (id, name, age) VALUES (1, 'Ксения', 22), (2, 'Лера', 23)"""
)  # вставляем записи в таблицу
cur.execute("SELECT * FROM users")  # читаем записи в бд
cur.execute(
    "UPDATE users SET name = 'Айсу', age = 21 WHERE id = 2"
)  # обновляем запись в бд и указываем какую именно строку обновлять
cur.execute("DELETE FROM users WHERE id = 2")  # удаляем запись с id = 2 в бд
con.commit()  # сохраняем изменения в бд
con.close()  # закрываем соединение с бд
