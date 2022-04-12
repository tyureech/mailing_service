import random
from celery import shared_task
from django.db.models import Q
from django.utils import timezone

from .models import MailingModel, ClientModel, MessageModel


@shared_task
def save_model():
    mailings = MailingModel.objects.filter(
        Q(time_start_mailing__lte=timezone.now()),
        Q(time_finish_mailing__gte=timezone.now()),
    )

    print('all {}'.format(MailingModel.objects.all()))
    print('filter {}'.format(mailings))
    print(timezone.now())
    return timezone.now()
