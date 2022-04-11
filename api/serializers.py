from rest_framework import serializers
from .models import MailingModel, ClientModel, MessageModel


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailingModel
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'
