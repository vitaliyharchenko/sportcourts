from django.contrib import admin
from models import Team, UserTeam


# Register your models here.
class UserTeamInline(admin.TabularInline):
    model = UserTeam
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [UserTeamInline]


admin.site.register(Team, TeamAdmin)