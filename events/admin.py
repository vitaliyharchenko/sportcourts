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


class UserGameActionInline(admin.TabularInline):
    model = UserGameAction
    extra = 0


class GameAdmin(BaseEventAdmin):
    model = Game
    inlines = [UserGameActionInline]


class GameTypeInline(admin.TabularInline):
    model = GameType
    extra = 0


class AmpluaInline(admin.TabularInline):
    model = Amplua
    extra = 0


class SportTypeAdmin(admin.ModelAdmin):
    model = SportType
    inlines = [GameTypeInline, AmpluaInline]

# Register your models here.
admin.site.register(SportType, SportTypeAdmin)
admin.site.register(Game, GameAdmin)