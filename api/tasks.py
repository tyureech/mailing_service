from celery import shared_task
from django.db.models import Q
from django.utils import timezone

from .models import MailingModel, ClientModel, MessageStatisticsModel, FilterCodePhoneTag
from .utils import Connections


@shared_task
def sending_mailing_list():
    mailings = MailingModel.objects.filter(
        Q(time_start_mailing__lte=timezone.now()),
        Q(time_finish_mailing__gte=timezone.now()),
    )
    ids_filter_tag_code = mailings.values_list('filter_code_phone_and_tag')
    filter_code_phone = FilterCodePhoneTag.objects.filter(id__in=ids_filter_tag_code)
    clients = ClientModel.objects.filter(
        code_phone__in=filter_code_phone.values_list('parameter1__code_phone'),
        tag__in=filter_code_phone.values_list('parameter2__tag')
    )
    connect = Connections()
    for client in clients:
        for mailing in mailings:
            response = connect.send(mailing.id, client.phone, mailing.text)
            MessageStatisticsModel.objects.create(
                date_time_creation=timezone.now(),
                status=True if response.status_code == 200 else False,
                mailing=mailing,
                client=client,
            )
    return response.status_code
