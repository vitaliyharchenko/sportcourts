# coding=utf-8
from django.contrib import admin
from models import Court, Place, City, Country, CourtType


# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Place)
admin.site.register(CourtType)
admin.site.register(Court)
#TODO: inline city, country in admin