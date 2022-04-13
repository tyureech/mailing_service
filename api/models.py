from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MailingModel(models.Model):
    time_start_mailing = models.DateTimeField()
    text = models.TextField()
    filter_code_phone_and_tag = models.ManyToManyField('FilterCodePhoneTag')
    time_finish_mailing = models.DateTimeField()


class ClientModel(models.Model):
    TIMEZONES = (
        ('MSK−1', 'Калининградское время (MSK−1)'),
        ('MSK±0', 'Московское время (MSK±0)'),
        ('MSK+1', 'Самарское время (MSK+1)'),
        ('MSK+2', 'Екатеринбургское время (MSK+2)'),
        ('MSK+3', 'Омское время (MSK+3)'),
        ('MSK+4', 'Красноярское время (MSK+4)'),
        ('MSK+5', 'Иркутское время (MSK+5)'),
        ('MSK+6', 'Якутское время (MSK+6)'),
        ('MSK+7', 'Владивостокское время (MSK+7)'),
        ('MSK+8', 'Магаданское время (MSK+8)'),
        ('MSK+9', 'Камчатское время (MSK+9)'),
    )

    phone = PhoneNumberField(null=False, blank=False, unique=True, region='RU')
    code_phone = models.CharField(max_length=3)
    tag = models.CharField(max_length=20)
    UTC = models.CharField(max_length=32, choices=TIMEZONES)

    def save(self, *args, **kwargs):
        phone = self.phone.as_e164
        self.code_phone = phone[2:5]
        CodePhoneModel.objects.get_or_create(
            code_phone=self.code_phone,
            defaults={
                'code_phone': self.code_phone
            }
        )
        TagModel.objects.get_or_create(
            tag=self.tag,
            defaults={
                'tag': self.tag
            }
        )
        return super().save(*args, **kwargs)


class CodePhoneModel(models.Model):
    code_phone = models.CharField(max_length=3)

    def __str__(self):
        return self.code_phone


class TagModel(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class FilterCodePhoneTag(models.Model):

    parameter1 = models.ForeignKey('CodePhoneModel', on_delete=models.CASCADE)
    parameter2 = models.ForeignKey('TagModel', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('parameter1', 'parameter2')

    def __str__(self):
        return f'id - {self.id}, code_phone - {self.parameter1.code_phone}, tag - {self.parameter2.tag}'


class MessageStatisticsModel(models.Model):
    date_time_creation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey('MailingModel', on_delete=models.CASCADE)
    client = models.ForeignKey('ClientModel', on_delete=models.CASCADE)
