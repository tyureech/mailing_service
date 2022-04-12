from rest_framework import serializers
from .models import MailingModel, ClientModel, MessageModel, FilterCodePhoneTag


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailingModel
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    # code_phone = serializers.ReadOnlyField()

    class Meta:
        model = ClientModel
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'


class FilterCodePhoneTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCodePhoneTag
        fields = '__all__'
