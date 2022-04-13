from rest_framework import serializers
from .models import MailingModel, ClientModel, MessageStatisticsModel, FilterCodePhoneTag, CodePhoneModel, TagModel


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailingModel
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModel
        fields = '__all__'
        read_only_fields = ['code_phone']


class MessageStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageStatisticsModel
        fields = '__all__'
        depth = 1


class FilterCodePhoneTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilterCodePhoneTag
        fields = '__all__'
        depth = 1


class IDFilterCodePhoneTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterCodePhoneTag
        fields = '__all__'
