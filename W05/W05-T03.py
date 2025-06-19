class Animal:  # создаём класс Animal
    def speak(self):  # определяем метод speak для класса Animal
        return "..."


class Dog(Animal):  # класс Dog, наследует от Animal
    def speak(self):  # переопределяем метод speak для класса Dog
        return "Woof!"  # возвращаем Woof!


class Cat(Animal):  # класс Cat, наследует от Animal
    def speak(self):  # переопределяет метод speak для класса Cat
        return "Meow!"  # возвращает Meow!


dog = Dog()  # создаём объект dog класса Dog
print(dog.speak())  # вызываем метод speak у объекта dog, выводим Woof!

cat = Cat()  # создаём объект cat класса Cat
print(cat.speak())  # вызываем метод speak у объекта cat, выводим Meow!
