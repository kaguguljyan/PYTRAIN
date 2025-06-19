class User:  # класс с именем User
    def __init__(self):
        self.__secret = "hidden"  # создаем приватное поле __secret и присваиваем ему значение "hidden"

    def get_secret(self):  # получаем значение приватного поля __secret
        return self.__secret  # возвращаем значение приватного поля __secret

    def set_secret(self, value):  # установливаем новое значение для приватного поля
        self.__secret = (
            value  # присваиваем новое значение value приватному полю __secret
        )


user = User()  # новый объект класса User присваиваем переменной user
print(user.get_secret())  # выводим hidden
user.set_secret(
    "new_secret"
)  # вызываем метод set_secret и передаём новое значение "new_secret"
print(user.get_secret())  # выводим new_secret
