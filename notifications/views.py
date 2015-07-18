from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from models import Notification
import datetime


# # Create your views here.
# @require_GET
# @login_required
# def notification_read(request, *args, **kwargs):
#     Notification.objects.filter(pk=kwargs['pk'], user_id=request.user.id).update(read=True)
#     if request.is_ajax():
#         return HttpResponse('')
#     else:
#         return redirect(notifications_view)
#
#
# @require_GET
# @login_required
# def notification_delete(request, *args, **kwargs):
#     pk = kwargs.get('pk', 0)
#     if pk:
#         Notification.objects.filter(pk=pk, user_id=request.user.id).delete()
#     else:
#         Notification.objects.filter(user_id=request.user.id, datetime__lte=datetime.datetime.now()).delete()
#     if request.is_ajax():
#         return HttpResponse('')
#     else:
#         return redirect(notifications_view)