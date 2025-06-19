class Animal:  # создаём класс Animal
    def speak(self):  # определяем метод speak для класса Animal
        return "..."


class Dog(Animal):  # класс Dog, наследует от Animal
    def speak(self):  # переопределяем метод speak для класса Dog
        return "Woof!"  # возвращаем Woof!


class Cat(Animal):  # класс Cat, наследует от Animal
    def speak(self):  # переопределяет метод speak для класса Cat
        return "Meow!"  # возвращает Meow!


def make_sound(animal):  # единая функция для работы с любым животным
    print(animal.speak())  # работает с любым объектом, у которого есть метод speak()


dog = Dog()  # новый объект класса Dog присваиваем переменной dog
cat = Cat()  # новый обьект класса Cat присваиваем переменной cat

make_sound(dog)  # вызываем make_sound для dog
make_sound(cat)  # вызываем make_sound для cat
