from __future__ import absolute_import
import os
from celery import Celery, shared_task

# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_service.settings')

# здесь вы меняете имя
app = Celery("mailing_service")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()


@shared_task()
def add(x, y):
    return x / y


app.conf.beat_schedule = {
    'test': {
        'task': 'api.tasks.save_model',
        'schedule': 15.0
    }
}
