import requests  # импортируем библиотеку для http запросов

params = {
    "key": "value",
    "key1": "value1",
}  # создаем словарь с параметрами, будем их передавать в запросе
resp = requests.get(
    "https://httpbin.org/get", params=params
)  # отправляем get запрос на указаный url с параметрами
print("Get запрос")
print(resp.json())  # выводим ответ сервера в json

resp1 = requests.post(
    "https://httpbin.org/post", json=params
)  # отправляем post запрос на указаный url с параметрами, преобразуем словарь в json строку
print("Post запрос")
print(resp1.json())  # выводим ответ сервера в json
