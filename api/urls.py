from rest_framework import routers

from .views import MailingAPIView, ClientAPIView, MessageAPIView


router = routers.DefaultRouter()

router.register('mailing', MailingAPIView, basename='mailing')
router.register('client', ClientAPIView, basename='client')
router.register('message', MessageAPIView, basename='message')

urlpatterns = router.urls
