import os

try:

    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['X-Frame-Options'] = 'ALLOW-FROM'
        return response
