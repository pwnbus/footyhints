from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from web.models import Team, Game
from footyhints.config import config


@cache_page(config.cache_expiration)
def table_data(request):
    data = []
    teams = Team.objects.all()
    for team in teams:
        data.append(
            {
                "name": team.name,
                "logo": team.logo,
                "place": team.place,
                "points": team.points,
                "played": team.played,
                "wins": team.wins,
                "draws": team.draws,
                "loses": team.loses,
                "goals_for": team.goals_for,
                "goals_against": team.goals_against,
                "goal_difference": team.goal_difference,
            }
        )
    return JsonResponse({"data": data})


@cache_page(config.cache_expiration)
def completed_games(request):
    data = []
    games = Game.objects.filter(finished=True)

    for game in games:
        game_data = {
            "home_team_id": game.home_team.id,
            "home_team_name": game.home_team.name,
            "away_team_id": game.away_team.id,
            "away_team_name": game.away_team.name,
            "start_time": game.start_time,
            "interest_score": game.interest_score,
            "date_from_start_time": game.date_from_start_time,
        }
        data.append(game_data)
    return JsonResponse({"data": data})


@cache_page(config.cache_expiration)
def teams_completed_games(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        ## todo clean this up
        raise Exception("Team does not exist")

    data = []
    games = team.games.filter(finished=True)
    for game in games:
        game_data = {
            "home_team_name": game.home_team.name,
            "home_team_id": game.home_team.id,
            "away_team_name": game.away_team.name,
            "away_team_id": game.away_team.id,
            "start_time": game.start_time,
            "interest_score": game.interest_score,
            "date_from_start_time": game.date_from_start_time,
        }
        data.append(game_data)
    return JsonResponse({"data": data})


@cache_page(config.cache_expiration)
def upcoming_games(request):
    data = []
    games = Game.objects.filter(finished=False)
    for game in games:
        game_data = {
            "home_team": {
                "id": game.home_team.id,
                "name": game.home_team.name,
            },
            "away_team": {
                "id": game.away_team.id,
                "name": game.away_team.name,
            },
            "start_time": game.start_time,
            "date_from_start_time": game.date_from_start_time,
        }
        data.append(game_data)
    return JsonResponse({"data": data})


@cache_page(config.cache_expiration)
def teams_upcoming_games(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        ## todo clean this up
        raise Exception("Team does not exist")

    data = []
    games = team.games.filter(finished=False)
    for game in games:
        game_data = {
            "home_team": {
                "id": game.home_team.id,
                "name": game.home_team.name,
            },
            "away_team": {
                "id": game.away_team.id,
                "name": game.away_team.name,
            },
            "start_time": game.start_time,
            "date_from_start_time": game.date_from_start_time,
        }
        data.append(game_data)
    return JsonResponse({"data": data})
