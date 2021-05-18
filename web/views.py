import os
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from web.models import Team, Competition, Game
from footyhints.config import config


def load_defaults():
    teams = Team.objects.all().order_by('name')
    competition = Competition.objects.all()[0]
    version = 'v-dev'
    if 'FOOTYHINTS_VERSION' in os.environ:
        version = os.environ['FOOTYHINTS_VERSION']
    return {
        "teams": teams,
        "competition": competition,
        "version": version,
        "last_updated": competition.last_updated,
    }


@cache_page(config.cache_expiration)
def index(request):
    context = load_defaults()
    context['finished_games'] = Game.objects.filter(finished=True)
    return render(request, 'index.html', context)


@cache_page(config.cache_expiration)
def team(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return redirect('/')
    context = load_defaults()
    context['team'] = team
    context['finished_games'] = team.games.filter(finished=True)
    return render(request, 'team.html', context)


def table(request):
    context = load_defaults()
    return render(request, 'table.html', context)
