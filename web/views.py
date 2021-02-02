import os
from django.shortcuts import render, redirect
from web.models import Team, Competition, Game


def load_defaults():
    teams = Team.objects.all().order_by('name')
    competition = Competition.objects.all()[0]
    version = 'v-dev'
    if 'FOOTYHINTS_VERSION' in os.environ:
        version = os.environ['FOOTYHINTS_VERSION']
    return {
        "teams": teams,
        "league": competition.name,
        "version": version,
        "last_updated": competition.last_updated,
    }


def index(request):
    context = load_defaults()
    context['finished_games'] = Game.objects.filter(finished=True)
    context['upcoming_games'] = Game.objects.filter(finished=False).order_by('start_time')[:10]
    return render(request, 'index.html', context)


def team(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return redirect('/')
    context = load_defaults()
    context['team'] = team
    context['finished_games'] = team.games.filter(finished=True)
    context['upcoming_games'] = team.games.filter(finished=False).order_by('start_time')[:6]
    return render(request, 'team.html', context)
