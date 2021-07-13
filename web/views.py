import os
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from web.models import Team, Competition
from footyhints.config import config

from .helpers import mobile_browser


def load_defaults(request):
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
        "mobile": mobile_browser(request)
    }


@cache_page(config.cache_expiration)
def index(request):
    context = load_defaults(request)
    return render(request, 'index.html', context)


@cache_page(config.cache_expiration)
def team(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return redirect('/')
    context = load_defaults(request)
    context['team'] = team
    return render(request, 'team.html', context)


@cache_page(config.cache_expiration)
def table(request):
    context = load_defaults(request)
    return render(request, 'table.html', context)
