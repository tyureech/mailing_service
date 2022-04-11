import random
from celery import shared_task

from .models import CeleryTest


@shared_task
def save_model():
    print(random.randint)
    obj = CeleryTest.objects.create(name=''.join([str(random.randint(0, 9)) for _ in range(10)]))
    return obj.name
