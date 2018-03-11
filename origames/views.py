from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from league import models
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    if request.method == "POST":
        race = models.Race.objects.first()
        if race.is_active:
            team = models.Team.objects.get(owner=request.user, belonged_race=race)
            if request.POST.get("add")=="":
                if team.selected_players.all().filter(player__name=request.POST.get("name")).count() != 0:
                    return redirect("home")
                name = request.POST.get("name")
                x = team.add_player(name)
                if x == 0:
                    messages.success(request, "Added "+name+" successfully!")
                elif x == 1:
                    messages.error(request, "Can't add more of the same group" )
                else:
                    messages.error(request, "Not enough money" )
                return redirect("home")

            if request.POST.get("remove")=="":
                if team.selected_players.all().filter(player__name=request.POST.get("name")).count() != 1:
                    return redirect("home")
                name = request.POST.get("name")
                try:
                    team.remove_player(name)
                except:
                    messages.error(request, "Can't do that" )
                else:
                    messages.success(request, "Removed "+name+" successfully!")
                    return redirect("home")
            return redirect("home")
    else:
        return redirect("league/results")
        if request.user.is_authenticated:
            race = models.Race.objects.first()
            try:
                team = models.Team.objects.get(owner=request.user, belonged_race=race)
                budget=team.budget
                team_players = team.selected_players.all().order_by("group", "-price", "-player__sex") ## this returns participation objects
                players_except_team = models.Participation.objects.filter(race=race).exclude(id__in=team_players).order_by("group", "-price", "-player__sex")
                return render(request, "wall.html",{"race":race,"team":team_players, "players":players_except_team, "budget": "{}".format(budget)})
            except:
                race = models.Race.objects.first()
                team = models.Team(owner=request.user, belonged_race=race)
                team.save()
                return redirect("home")
        else:
            return render(request, "home.html")
    redirect("home")

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html")

    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request, "login.html")


@login_required
def logout(request):
    django_logout(request)
    return redirect("login")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
