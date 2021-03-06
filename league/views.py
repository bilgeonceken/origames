from django.shortcuts import render
from django.http import HttpResponse
from . import forms, models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PlayerCreateView(generic.CreateView):
    model = models.Player
    template_name = "league/create_player.html"
    form_class = forms.PlayerForm
    success_url='create_player'


## LISTS ALL PLAYERS. WE SHOW ONLY CURRENT RACE'S PLAYERS NOW
# class PlayersListView(generic.ListView):
#     model = models.Player
#     template_name = "league/player_list.html"
#     context_object_name = "players"
#     # context["other_things"]=["thing1", "thing2"] --> Possible to add other stuff to ctx

@method_decorator(login_required, name='dispatch')
class PlayersListView(generic.ListView):
    ## modified get_queryset method in order to use the qset we want
    ## since we want more than just a model = models.Player
    def get_queryset(self):
        race = models.Race.objects.first()
        # print(models.Participation.objects.filter(race=race))
        return models.Participation.objects.filter(race=race).order_by("group", "-price" ,"-player__sex")

    template_name = "league/player_list.html"
    context_object_name = "players"
    # context["other_things"]=["thing1", "thing2"] --> Possible to add other stuff to ctx


def stages(request):
    stages = models.Race.objects.first().stages.all()
    return render(request, "stages.html", {"stages": stages})

def rules(request):
    return render(request, "rules.html")

@login_required
def results(request):
    race = models.Race.objects.first()
    teams = models.Team.objects.filter(belonged_race=race, total_score__gt=0).order_by("-total_score")
    participations = models.Participation.objects.filter(race=race).order_by("-total_score")
    return render(request, "league/results.html", {"teams": teams, "participations": participations})
