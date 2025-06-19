class Animal:  # создаём класс Animal
    def sound(self):  # определяем метод sound для класса Animal
        return "..."

    def feed(self):  # определяем метод feed для класса Animal
        return "..."

    def sleep(self):  # определяем метод sleep для класса Animal
        return "..."


class Lion(Animal):  # класс Lion, следует от Animal
    def sound(self):  # переопределяем метод sound для класса Lion
        return "RRR"  # возвращаем RRR

    def feed(self):  # переопределяем метод feed для класса Lion
        return "meat"  # возвращаем maet

    def sleep(self):  # переопределяем метод sleep для класса Lion
        return "zzz"  # возвращаем zzz


class Tiger(Animal):  # класс Tiger, следует от Animal
    def sound(self):  # переопределяем метод sound для класса Tiger
        return "GRR"  # возвращаем GRR

    def feed(self):  # переопределяем метод feed для класса Tiger
        return "meat"  # возвращаем meat

    def sleep(self):  # переопределяем метод sleep для класса Tiger
        return "ZZZ"  # возвращаем ZZZ


def make_sound(animal):  # единая функция для работы с любым животным
    print(animal.sound())  # с любым объектом, у которого есть метод sound()

    print(animal.feed())  # с любым объектом, у которого есть метод fead()

    print(animal.sleep())  # с любым объектом, у которого есть метод sleep()


lion = Lion()  # класса Lion присваиваем перемнной lion
tiger = Tiger()  # класса Tiger присваиваем переменной Tiger

make_sound(lion)  # вызываем make_sound для lion
make_sound(tiger)  # вызываем make_sound для tiger
