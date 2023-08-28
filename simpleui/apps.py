from django.apps import AppConfig


class SimpleApp(AppConfig):
    name = 'simpleui'

    def ready(self):
        # 如果是django3+ 就使用中间件，删除header中的X-Frame-Options

        try:
            import django
            version = django.get_version()
            if int(version.split('.')[0]) >= 3:
                from django.conf import settings
                for index, item in enumerate(settings.MIDDLEWARE):
                    if item == 'django.middleware.clickjacking.XFrameOptionsMiddleware':
                        settings.MIDDLEWARE.pop(index)

        except Exception as e:
            pass
        pass
