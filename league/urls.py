from django.urls import path, include
from . import views;

app_name = "league"

urlpatterns = [
    path("players/", views.PlayersListView.as_view(), name="player_list"),
    path("players/create_player", views.PlayerCreateView.as_view(), name="create_player"),
    path("stages", views.stages, name="stages"),
    path("rules", views.rules, name="rules"),
    path("results", views.results, name="results"),
    # path("create_player", views.create_player, name="create_player"),
]
