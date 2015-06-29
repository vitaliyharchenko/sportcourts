from django.shortcuts import render
from models import Team, UserTeam


# Create your views here.
def teamslist(request):
    context = {'teams': Team.objects.all()}
    return render(request, 'teams.html', context)


def teamdetail(request, team_id):
    team = Team.objects.get(id=team_id)
    context = {'team': team,
               'userteams': UserTeam.objects.filter(team=team)}
    return render(request, 'team.html', context)