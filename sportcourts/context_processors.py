from django.conf import settings


def variables(request):
    return {'YANDEX_MAPS_API_KEY': settings.YANDEX_MAPS_API_KEY}