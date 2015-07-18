from models import Notification
from django.utils import timezone


def notifications(request):
    query = Notification.objects.filter(user_id=request.user.id, datetime__lte=timezone.now())
    new_count = query.filter(read=0).count()
    if new_count:
        query = query.filter(read=0)
    context = dict()
    context['notifications_count'] = len(query)
    context['notifications'] = query
    return context