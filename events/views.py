from django.shortcuts import render
from models import Event


# Create your views here.
def events(request):
    context = {'events': Event.objects.all()}
    return render(request, 'events.html', context)