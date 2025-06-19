# создаём файл с тестами

# импортируем код, который хотим протестировать, в тестовый файл

from W06_T02 import sum_two_numbers, is_even, greet, multiply_list, find_max

# тестируем ф-ию суммы двух чисел


def test_sum_two_numbers():
    assert sum_two_numbers(2, 3) == 5
    assert sum_two_numbers(-2, 5) == 3
    assert sum_two_numbers(0, 0) == 0


# тестируем ф-ию проверки числа на четность


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


# тестируем ф-ию для вывода приветствия


def test_greet():
    assert greet("jp") == "Привет, jp!"
    assert greet("") == "Привет, !"


# тестируем ф-ию, умножающию все числа в списке


def test_multiply_list():
    assert multiply_list([1, 2, 3]) == 6
    assert multiply_list([-2, 6, 1]) == -12
    assert multiply_list([0, 1, 2]) == 0
    assert multiply_list([]) == 1


# тестируем ф-ию, ищущая максимальное число из списка


def test_find_max():
    assert find_max([1, 3, 2]) == 3
    assert find_max([-3, -2, -1]) == -1
