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


def parse_game(game):
    questions = []
    for question in game.sorted_questions:
        question_dict = {
            "description": question.description,
            "answer": question.answer,
        }
        questions.append(question_dict)
    score_modifications = []
    for score_modification in game.sorted_score_modifications:
        score_modifications_dict = {
            "value": score_modification.value,
            "priority": score_modification.priority,
            "reason": score_modification.reason,
        }
        score_modifications.append(score_modifications_dict)
    return {
        "id": game.id,
        "home_team": {
            "id": game.home_team.id,
            "name": game.home_team.name,
            "logo": game.home_team.logo,
            "score": game.home_team_score,
        },
        "away_team": {
            "id": game.away_team.id,
            "name": game.away_team.name,
            "logo": game.away_team.logo,
            "score": game.away_team_score,
        },
        "start_time": game.start_time,
        "stadium": game.stadium,
        "city": game.city,
        "referee": game.referee,
        "highlights_url": game.highlights_url,
        "interest_level": game.interest_level,
        "interest_score": game.interest_score,
        "date_from_start_time": game.date_from_start_time,
        "questions": questions,
        "score_modifications": score_modifications,
    }


@cache_page(config.cache_expiration)
def completed_games(request):
    data = []
    games = Game.objects.filter(finished=True)

    for game in games:
        data.append(parse_game(game))
    return JsonResponse({"data": data})


@cache_page(config.cache_expiration)
def teams_completed_games(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return JsonResponse({'status': 'false', 'message': "Team does not exist"}, status=500)

    data = []
    games = team.games.filter(finished=True)
    for game in games:
        data.append(parse_game(game))
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
        return JsonResponse({'status': 'false', 'message': "Team does not exist"}, status=500)

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
