# coding=utf-8
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')