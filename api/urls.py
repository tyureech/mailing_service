from rest_framework import routers

from .views import MailingAPIView, ClientAPIView, MessageStatisticsAPIView, FilterCodePhoneTagAPIView


router = routers.DefaultRouter()

router.register('mailing', MailingAPIView, basename='mailing')
router.register('client', ClientAPIView, basename='client')
router.register('message-statistics', MessageStatisticsAPIView, basename='message-statistics')
router.register('filter-code-phone-tag', FilterCodePhoneTagAPIView, basename='filter-code-phone-tag')

urlpatterns = router.urls
