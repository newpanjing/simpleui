from django.http import HttpResponse

try:

    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):

    @staticmethod
    def process_response(self, response):
        if response and isinstance(response, HttpResponse):
            response['X-Frame-Options'] = 'ALLOW-ALL'
        return response
