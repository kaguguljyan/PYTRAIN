import requests
from bs4 import BeautifulSoup

url = "https://news.mail.ru/"  # адрес сайта, с которого выгружаются данные

r = requests.get(url)  # отправляем Get запрос на указанный url
soup = BeautifulSoup(
    r.content, "html.parser"
)  # парсер BeautifulSoup, который принимает r.content (HTML код) и "html.parser" (встроенный парсер Python для разбора HTML)

rss_links = soup.find_all(
    "link", {"rel": "alternate", "type": "application/rss+xml"}
)  # ищем в HTML все теги link, у которых атрибут rel равен "alternate" и атрибут type равен "application/rss+xml", find_all возвращает список всех таких тегов

for link in rss_links:  # пробегаем по каждому найденному тегу link из списка
    title = link.get("title")  # извлекаем атрибут title
    href = link.get("href")  # извлекаем атрибут href
    print(f"{title}: {href}")  # выводим на экран строку с названием и ссылкой
