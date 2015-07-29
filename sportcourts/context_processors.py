from django.conf import settings


def variables(request):
    return {'current_url': request.get_full_path,
            'return_url': request.META.get('HTTP_REFERER', '/')}