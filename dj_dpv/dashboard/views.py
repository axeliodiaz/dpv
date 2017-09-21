from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

from utils.views import get_description_user, get_bs, get_peso
from api.wrappers import base_request


class Dashboard(TemplateView):
    """docstring for Dashboard."""
    template_name = 'stats.html'

    def get_context_data(self, **kwargs):
        """Metodo para retornar context al metodo get

        :param kwargs:
        :return: context
        """
        context = super().get_context_data(**kwargs)
        try:
            description = get_description_user(settings.BS_INFO_FROM)
            bs = get_bs(description)
            peso = get_peso()
            print("Bs: {} y Pesos: {}".format(bs, peso))
            import pdb; pdb.set_trace() 
            divisas = base_request('divisas')
            context['bolivares'] = bs

            return context
        except KeyError:
            raise
