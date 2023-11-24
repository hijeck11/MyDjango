# MyDjango

Домашка на среду 22.11.2023:
1. Скрыть пароли
    -Создал в корне проекта файл .env;
    -pip install python-decouple;
    -pip install config;
    -в файле .env создал переменные с логином и паролем от БД. Переменную SECRET_KEY;
    -в файле проекта settings.py выполнил:
        from decouple import config;
        заменил значения SECRET_KEY = config('SECRET_KEY')
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        

2. Заполнить базу фэйковыми данными.
3. Сделать сигнал который отслеживает сохранение и удаление данных.  И отправляет сообщение в телеграмм.
    -добавлен сигнал на уведобление ТГ бот при добавление или удалении данных в модели Labriary