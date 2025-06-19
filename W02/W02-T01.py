a = [1, 6, 4, 2, 3, 5]

# фильтрация по чётности


def is_even(num):
    b = []  # создаём пустой список, чтобы потом добавлять в него чётные числа
    for i in num:  # проходим по списку
        if i % 2 == 0:  # если число делится на 2 без остатка,
            b.append(i)  # то добавляем к пустому списку это число
    return b  # возвращаем список чётных чисел


print(is_even(a))

# сортировка


def sort(num):
    return sorted(num)  # возвращаем сортированные список с помощью метода sorted()


print(sort(a))

# реверс


def reverse_list(num):
    num.reverse()  # переворачиваем список с помощью метода reserve()
    return num  # возвращаем перевёрнутый список


print(reverse_list(a))

# среднее значение


def average_value(num):
    e = (sum(num)) / (len(num))  # находим среднее число
    return e  # возвращаем его


print(average_value(a))

# поиск максимального


def find_max(num):
    print(max(num))  # находим максимум с помощью


find_max(a)
