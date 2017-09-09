from django.shortcuts import render
from django.views.generic.base import TemplateView
from utils.views import get_description_user, get_bs


class Dashboard(TemplateView):
    """docstring for Dashboard."""
    template_name = 'stats.html'

    def get(self, request, **kwargs):
        description = get_description_user('dolartoday')
        bs = get_bs(description)

        import pdb; pdb.set_trace()
        return render(request, template_name=self.template_name, context={})
