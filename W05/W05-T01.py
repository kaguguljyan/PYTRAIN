class Person:  # создаём класс Person
    def __init__(
        self, name, age
    ):  # создаём функцию с методом __init__, self- ссылка на текущий обьект класса
        self.name = name  # сохраняем имя в name
        self.age = age  # сохраняем возраст в age

    def greet(self):  # функция приветствия greet
        print(f"Привет, {self.name}")


a = Person("Вася", 20)  # обьект класса Person

print(a.name)  # обращение к name и age
print(a.age)

a.greet()  # вызываем метод
