from django.shortcuts import render
from models import Court


# Create your views here.
def courtlist(request):
    context = {'courts': Court.objects.all()}
    return render(request, 'courts.html', context)


def court(request, court_id):
    court = Court.objects.get(id=court_id)
    context = {'court': court}
    court.views += 1
    court.save()
    return render(request, 'court.html', context)