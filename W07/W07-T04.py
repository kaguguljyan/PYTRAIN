from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""
soup = BeautifulSoup(
    html_doc, "html.parser"
)  # создём обьект soup и парсим документ HTML
print(soup.text)  # возвращаем весь текст
print(soup.title)  # обращаемся к тегу title
print(soup.title.name)  # возвращаем название тега
print(soup.title.string)  # возвращаем текст внутри тега
print(soup.title.parent.name)  # возвращаем название родительского тега
print(soup.p)  # обращаемся к первому тегу p
print(
    soup.p["class"]
)  # возвращаем значение class в виде списка (т.к. классов может быть больше)
print(soup.a)  # обращаемся к первому тегу a
print(soup.find_all("a"))  # возвращаем все теги a
print(soup.find_all("p"))  # возвращаем все теги p
print(soup.find(id="link3"))  # находим элемент с id = "link3"
