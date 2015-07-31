# coding=utf-8
from django.shortcuts import render
from events.views import events


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return events(request)
    else:
        return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')