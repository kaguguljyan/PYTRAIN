# приветствие
a = input("Введите имя: ")  # пользователь вводит имя


def greet(name):
    return f"Hello, {name}"  # возвращает приветствие с именем


print(greet(a))

# сумма двух чисел

b = int(input("Первое слагаемое: "))  # пользователь вводит первое слагаемое
c = int(input("Второе слагаемое: "))  # вводит второе слагаемое


def sum(b, c):
    return b + c  # возвращает сумму двух чисел


print(sum(b, c))

# длинна слова

d = input("Введите слово: ")  # пользователь вводит слово


def longest_word(word):
    return len(word)  # возвращает длину слова


print(longest_word(d))

# степень двойки

e = int(input("Введите степень: "))  # пользователь вводит степень


def degree_of_two(num):
    return 2**num  # возвращает степень двойки


print(degree_of_two(e))

# первая буква слова

f = input("Введите слово: ")  # пользователь вводит слово


def first_letter(lt):
    return lt[0]  # возвращает первую букву


print(first_letter(f))

# проверка палиндрома

g = input("Введите слово: ")  # пользователь вводит слово


def palindrome(word):
    if (
        word == word[::-1]
    ):  # если слово равно его перевёрнутой версии, то возвращаем True
        return True
    else:  # иначе False
        return False


print(palindrome(g))
