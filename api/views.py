from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import MailingModel, ClientModel, MessageModel, FilterCodePhoneTag
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer, FilterCodePhoneTagSerializer


class MailingAPIView(ModelViewSet):
    queryset = MailingModel.objects.all()
    serializer_class = MailingSerializer


class ClientAPIView(ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer


class MessageAPIView(ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class FilterCodePhoneTagAPIView(ModelViewSet):
    queryset = FilterCodePhoneTag.objects.all()
    serializer_class = FilterCodePhoneTagSerializer

