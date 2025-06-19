# сначала пишем код с ошибками


def hello(name="World"):
    """Say hello"""
    greeting = f"Hello, {name}!"
    print(greeting)


# проверяем есть ли ошибки с помощью flake8
# затем исправляем ошибки с помощью black и получается


def hello(name="World"):
    """Say hello"""
    greeting = f"Hello, {name}!"
    print(greeting)
