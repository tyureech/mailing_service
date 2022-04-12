from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MailingModel(models.Model):
    time_start_mailing = models.DateTimeField()
    message_text = models.TextField()
    filter_code_phone_and_tag = models.ManyToManyField('FilterCodePhoneTag')
    time_finish_mailing = models.DateTimeField()


class ClientModel(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True, region='RU')
    code_phone = models.CharField(max_length=3)
    tag = models.CharField(max_length=20)
    UTC = models.CharField(max_length=20)

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


class TagModel(models.Model):
    tag = models.CharField(max_length=20)


class FilterCodePhoneTag(models.Model):
    code_phone = models.ForeignKey('CodePhoneModel', on_delete=models.CASCADE)
    tag = models.ForeignKey('TagModel', on_delete=models.CASCADE)


class MessageModel(models.Model):
    date_time_creation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey('MailingModel', on_delete=models.CASCADE)
    client = models.ForeignKey('ClientModel', on_delete=models.CASCADE)
