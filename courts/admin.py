# coding=utf-8
from django.contrib import admin
from models import Court, Place, City, Region, Country, CourtType


# Register your models here.
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Place)
admin.site.register(CourtType)
admin.site.register(Court)
#TODO: inline city, country in admin