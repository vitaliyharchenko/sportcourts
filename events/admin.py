# coding=utf-8
from django.contrib import admin
from models import Event, SportType, GameType, Game, UserGameAction, Amplua


# Register your models here.
class BaseEventAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by']

    def save_model(self, request, obj, form, change):
        user = request.user
        obj.created_by = user
        print user.id
        obj.save()


class EventAdmin(BaseEventAdmin):
    model = Event


class GameAdmin(BaseEventAdmin):
    model = Game

# Register your models here.
admin.site.register(SportType)
admin.site.register(GameType)
admin.site.register(Game, GameAdmin)
admin.site.register(UserGameAction)
admin.site.register(Amplua)