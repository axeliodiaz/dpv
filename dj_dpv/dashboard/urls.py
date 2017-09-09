from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='stats.html')),
]
