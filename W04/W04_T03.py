import main  # импортируем модуль main
from main import c  # импортируем из модуля main переменную c
import main as mx  # импортируем модуль main с псевдонимом mx
import platform  # импортируем стандартный модуль platform

a = int(input("Число 1: "))  # вводим два числа
b = int(input("Число 2: "))


def sum_num(a, b):  # функиця суммы двух чисел
    print(a + b)


sum_num(a, b)

d = main.c[
    0
]  # берём первый элемент списка c, который определён в модуле main, и выводит его. Здесь используется import main
print(d)

print(
    c[0]
)  # выводим первый элемент переменной c, импортированной из модуля main через from main import

c = [1, 2, 3]
print(
    c[0]
)  # создаём новый список c, который перекрывает ранее импортированную из main переменную c

e = mx.c[0]  # используем псевдоним mx
print(e)

f = (
    platform.system()
)  # вызываем функцию system() из модуля platform, которая возвращает название ос
print(f)

g = dir(
    platform
)  # функция dir() возвращает список всех атрибутов и методов модуля platform
print(g)

main.sum_num(
    5, b
)  # вызываем функцию sum_num из модуля main. Передаём ей аргументы 5 и b
