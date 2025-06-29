# создадим файл с ф-ми, которые будем тестировать

# функция суммы двух чисел


def sum_two_numbers(a, b):  # принимаем параметры
    return a + b  # возвращаем сумму


# функция, проверяющая чётное ли число


def is_even(number):
    if number % 2 == 0:  # проверяем остаток от деления на 2
        return True  # если делится без остатка, значит число чётное. Возвращаем True
    else:  # иначе False
        return False


# функция для вывода приветствия


def greet(name):
    return f"Привет, {name}!"  # возвращаем приветствие


# функция, умножающая все числа в списке


def multiply_list(list):
    s = 1  # счетчик
    for num in list:  # пробегаем по всем числам в списке
        s *= num  # умножаем текущий результат на число
    return s  # возвращаем результат


# функция, ищущая максимальное число из списка


def find_max(num):
    return max(num)  # преобразуем в числа и находим максимум
