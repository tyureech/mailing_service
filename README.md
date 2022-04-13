# mailing_service

Запуск проекта:

1 . Активируем виртульнок оеружение.

2 . Скачиваем пакеты:

    pip install -r req.txt

3 . Создаем базу данных:

    python3 manage.py makemigrations

    python3 manage.py migrate

4 . Запускаем сервер:

    python3 manage.py runserver
    
    brew services start redis / sudo systemctl start redis # mac/linux
    
    celery -A mailing_service beat
    
    celery -A mailing_service worker -l INFO

По ссылке http://127.0.0.1:8000/api создаем пользователя,
фильтр рассылки и саму рассылку. Так же там можно посмотреть статистику по рассылкам.
