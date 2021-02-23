from django.contrib import admin
from django.urls import path
from web.views import index, team, table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('team/<int:team_id>/', team),
    path('table', table),
]
