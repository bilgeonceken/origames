from django.shortcuts import render
from django.http import HttpResponse
from . import forms, models
from django.views import generic


class PlayerCreateView(generic.CreateView):
    model = models.Player
    template_name = "league/create_player.html"
    form_class = forms.PlayerForm
    success_url='create_player'


class PlayersListView(generic.ListView):
    model = models.Player
    template_name = "league/player_list.html"
    context_object_name = "players"
    # context["other_things"]=["thing1", "thing2"] --> Possible to add other stuff to ctx
