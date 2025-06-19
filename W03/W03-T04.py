# факториал
a = int(input("Введите число: "))


# задаётся рекурентной формулой
def factorial(num):

    if num == 0:  # если факториал равен 0, то возвращаем 1
        return 1
    else:  # иначе возвращаем факториал числа
        return num * factorial(num - 1)


print(factorial(a))

# числа Фибоначчи
b = int(input("Введите число: "))


# последовательность чисел Фибоначчи задаётся линейным рекуррентным соотношением
def Fibonachi(num):
    if num == 0:  # если число равно 0, то возвращаем 0
        return 0
    elif num == 1:  # если число равно 1, то возвращаем 1
        return 1
    else:  # иначе возвращаем число Фибоначчи
        return Fibonachi(num - 1) + Fibonachi(num - 2)


print(Fibonachi(b))
