import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
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
    base_template = 'base_generic.html'
    if mobile_browser(request):
        base_template = 'base_mobile.html'
    return {
        "teams": teams,
        "competition": competition,
        "version": version,
        "last_updated": competition.last_updated,
        "base_template": base_template,
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


def info(request):
    context = load_defaults(request)
    info = {
        "version": context['version'],
        "base_template": context['base_template'],
        "last_updated": context['last_updated'],
        "mode": config.mode,
        "cache_enabled": config.cache_enabled,
        "cache_expiration": config.cache_expiration,
        "web_debug": config.web_debug,
    }
    return JsonResponse(info)
