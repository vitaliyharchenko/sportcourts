from django.shortcuts import render
from models import Court


# Create your views here.
def courtlist(request):
    context = {'courts': Court.objects.all()}
    return render(request, 'courts.html', context)


def court(request, court_id):
    context = {'court': Court.objects.get(id=court_id)}
    return render(request, 'court.html', context)