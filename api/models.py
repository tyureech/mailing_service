from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.modelfields import PhoneNumberField


class MailingModel(models.Model):
    time_start_mailing = models.DateTimeField()
    code_phone = models.IntegerField()
    tag = models.CharField(max_length=20)
    filter_code_phone = models.CharField(max_length=20)
    time_finish_mailing = models.DateTimeField()


class ClientModel(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True, region='RU')
    code_phone = models.IntegerField(max_length=3)
    tag = models.CharField(max_length=20)
    UTC = models.CharField(max_length=20)


class MessageModel(models.Model):
    date_time_creation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey('MailingModel', on_delete=models.CASCADE)
    client = models.ForeignKey('ClientModel', on_delete=models.CASCADE)