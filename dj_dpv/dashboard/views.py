from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

from utils.views import get_description_user, get_bs, get_peso


class Dashboard(TemplateView):
    """docstring for Dashboard."""
    template_name = 'stats.html'

    def get(self, request, **kwargs):
        description = get_description_user(settings.BS_INFO_FROM)
        bs = get_bs(description)
        peso = get_peso()
        print("Bs: {} y Pesos: {}".format(bs, peso))
        return render(request, template_name=self.template_name, context={})
