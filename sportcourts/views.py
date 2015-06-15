# coding=utf-8
from django.shortcuts import render


# Create your views here.
def index(request):
    user = request.user
    args = {'user': user}
    return render(request, 'index.html', args)