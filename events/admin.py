# coding=utf-8
from django.contrib import admin
from models import Event, SportType, GameType


# Register your models here.
class EventAdmin(admin.ModelAdmin):

    model = Event
    readonly_fields = ['created_by']

    def save_model(self, request, obj, form, change):
        user = request.user
        obj.created_by = user
        print user.id
        obj.save()

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(SportType)
admin.site.register(GameType)