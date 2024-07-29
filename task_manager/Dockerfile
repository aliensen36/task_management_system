# Используем официальный образ Python 3.12 в качестве базового образа
FROM python:3.12

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /code/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . /code/

# Выполняем миграции и запускаем сервер
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
