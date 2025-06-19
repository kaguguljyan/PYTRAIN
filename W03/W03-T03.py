from functools import reduce  # для reduce импортируем библиотеку

x = map(lambda a: a**2, [1, 2, 3])  # применяет функцию к каждому элементу
print(list(x))

y = filter(
    lambda b: b * 2 == 2, [1, 2, 3]
)  # фильтрует элементы коллекции и оставляет элементы, подходящие по условию
print(list(y))

z = reduce(lambda c, d: c + d, [1, 2, 3])  # складывает коллекцию в одно значение
print(z)
