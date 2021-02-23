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
        "competition": competition,
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


def table(request):
    context = load_defaults()
    table_data = []
    for team in context['teams']:
        games_info = team.games_info
        goals_info = team.goals_info
        table_data.append(
            {
                "name": team.name,
                "logo": team.logo,
                "place": team.place,
                "points": team.points,
                "played": games_info['played'],
                "wins": games_info['wins'],
                "draws": games_info['draws'],
                "loses": games_info['loses'],
                "goals_for": goals_info['goals_for'],
                "goals_against": goals_info['goals_against'],
                "goal_difference": goals_info['goal_difference'],
            }
        )
    context['table_data'] = table_data
    return render(request, 'table.html', context)
