import logging
from django.conf import settings
from django.views import generic
from rest_framework import viewsets, views, response, status, permissions, filters
from rest_framework.generics import ListAPIView


logger = logging.getLogger('{0}'.format(__name__))


class BaseView(generic.TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update({})
        return self.render_to_response(context)
