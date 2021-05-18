from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from web.models import Team
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
