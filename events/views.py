# coding=utf-8
from django.shortcuts import render
from models import Event
from customuser import User


# Create your views here.
def events(request):
    context = {'events': Event.objects.all()}
    try:
        if request.user.is_authenticated():
            user = User.objects.get(email=request.user.email)
            context['current_user'] = user
        else:
            context['current_user'] = None
    except User.DoesNotExist:
        pass
    return render(request, 'events.html', context)