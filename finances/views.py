from django.shortcuts import render
from events.models import Game


# Create your views here.
def fin(request):
    context = {'games': Game.objects.all()}
    return render(request, 'fin.html', context)