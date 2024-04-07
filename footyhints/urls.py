from django.urls import path

from web.views import index, team, table, info
from web.api import table_data, completed_games, teams_completed_games, upcoming_games, teams_upcoming_games


urlpatterns = [
    path('', index),
    path('team/<int:team_id>/', team),
    path('table', table),
    path('api/table', table_data),
    path('api/completed_games', completed_games),
    path('api/completed_games/<int:team_id>', teams_completed_games),
    path('api/upcoming_games', upcoming_games),
    path('api/upcoming_games/<int:team_id>', teams_upcoming_games),
    path('info', info),
]
