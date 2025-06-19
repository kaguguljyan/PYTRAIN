# базовый образ Python
FROM python:3.10-slim


# установка рабочей директории
WORKDIR /app


# копирование файлов проекта в контейнер
COPY requirements.txt .


# установка зависимости 
RUN pip install -r requirements.txt


# копирование остальных файлов
COPY . .


# запуск скрипта при старте контейнера
CMD ["python", "W09-T03.py"]