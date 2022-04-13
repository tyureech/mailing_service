from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters import rest_framework as filters

from .models import MailingModel, ClientModel, MessageStatisticsModel, FilterCodePhoneTag
from .serializers import MailingSerializer, ClientSerializer, MessageStatisticsSerializer, FilterCodePhoneTagSerializer, \
    IDFilterCodePhoneTagSerializer


class MailingAPIView(ModelViewSet):
    queryset = MailingModel.objects.all()
    serializer_class = MailingSerializer


class ClientAPIView(ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer


class MessageStatisticsAPIView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = MessageStatisticsModel.objects.all()
    serializer_class = MessageStatisticsSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('status', )


class FilterCodePhoneTagAPIView(ModelViewSet):
    queryset = FilterCodePhoneTag.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return FilterCodePhoneTagSerializer
        return IDFilterCodePhoneTagSerializer
