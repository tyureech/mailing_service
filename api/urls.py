from django.conf.urls import url
from django.urls import path, re_path
from rest_framework import routers, permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from .views import MailingAPIView, ClientAPIView, MessageStatisticsAPIView, FilterCodePhoneTagAPIView


router = routers.DefaultRouter()

router.register('mailing', MailingAPIView, basename='mailing')
router.register('client', ClientAPIView, basename='client')
router.register('message-statistics', MessageStatisticsAPIView, basename='message-statistics')
router.register('filter-code-phone-tag', FilterCodePhoneTagAPIView, basename='filter-code-phone-tag')

schema_view = get_schema_view(
    openapi.Info(
        title="Mailing Service",
        default_version='v1',
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
