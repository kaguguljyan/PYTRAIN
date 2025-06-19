import logging

# создаем логгер
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # устанавливаем самый низкий уровень для логгера

# создаем форматтер
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# создаем обработчики и настраиваем их
debug_handler = logging.FileHandler("debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

info_handler = logging.FileHandler("info.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = logging.FileHandler("errors.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# добавляем обработчики к логгеру
logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)
