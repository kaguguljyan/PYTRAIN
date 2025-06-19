import pdb  # импортируем библиотеку для дебага

# функция суммы двух чисел


def sum_two_numbers(a, b):  # принимаем параметры

    pdb.set_trace()
    print(f"{a} + {b} = {a + b}")
    return a + b  # возвращаем сумму


print(sum_two_numbers(1, 1))


# функция, проверяющая чётное ли число


def is_even(number):

    pdb.set_trace()
    if number % 2 == 0:  # проверяем остаток от деления на 2
        print(f"{number} чётное")
        return True  # если делится без остатка, значит число чётное. Возвращаем True
    else:  # иначе False
        print(f"{number} нечётное")
        return False


print(is_even(1))


# функция для вывода приветствия


def greet(name):

    pdb.set_trace()
    g = f"Привет, {name}!"
    print(f"Приветствие: '{g}'")
    return g  # возвращаем приветствие


print(greet("jfd"))


# функция, умножающая все числа в списке


def multiply_list(list):

    pdb.set_trace()
    s = 1  # счетчик
    print(f"s = {s}")
    for num in list:  # пробегаем по всем числам в списке
        s *= num  # умножаем текущий результат на число
        print(f"После умножения {num}, s = {s}")
    print(f"Результат: {s}")
    return s  # возвращаем результат


print(multiply_list([1, 2, 3]))


# функция, ищущая максимальное число из списка


def find_max(num):

    pdb.set_trace()
    m = max(num)
    print(f"Лист = {num}, максимум = {m}")
    return m  # преобразуем в числа и находим максимум


print(find_max([1, 2, 3]))
