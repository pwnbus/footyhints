from django.contrib import admin
from django.urls import path
from web.views import index, team

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('team/<int:team_id>/', team),
]
