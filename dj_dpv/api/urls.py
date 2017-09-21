from django.conf.urls import url, include
from .views import TipoDivisa
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'divisas',
                TipoDivisa,
                base_name='divisas')

urlpatterns = [
    url(r'^', include(router.urls)),
]
