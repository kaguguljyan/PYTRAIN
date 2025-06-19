# создаём Dockerfile 

# базовый образ Python
FROM python:3.10-slim

# копирование файлов проекта в контейнер
COPY . /app

# установка рабочей директории
WORKDIR /app

# запуск скрипта при старте контейнера
CMD ["python", "W09-T01.py"]