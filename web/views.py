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
        num_played = 0
        num_wins = 0
        num_draws = 0
        num_loses = 0
        num_goals_for = 0
        num_goals_against = 0
        for game in team.games.filter(finished=True):
            num_played += 1
            if game.home_team == team:
                num_goals_for += game.home_team_score
                num_goals_against += game.away_team_score
                if game.home_team_score > game.away_team_score:
                    num_wins += 1
                elif game.home_team_score == game.away_team_score:
                    num_draws += 1
                else:
                    num_loses += 1
            elif game.away_team == team:
                num_goals_against += game.home_team_score
                num_goals_for += game.away_team_score
                if game.away_team_score > game.home_team_score:
                    num_wins += 1
                elif game.away_team_score == game.home_team_score:
                    num_draws += 1
                else:
                    num_loses += 1

        table_data.append(
            {
                "name": team.name,
                "logo": team.logo,
                "place": team.place,
                "points": team.points,
                "played": num_played,
                "wins": num_wins,
                "draws": num_draws,
                "loses": num_loses,
                "goals_for": num_goals_for,
                "goals_against": num_goals_against,
                "goal_difference": num_goals_for - num_goals_against,
            }
        )
    context['table_data'] = table_data
    return render(request, 'table.html', context)
