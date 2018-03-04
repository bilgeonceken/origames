from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from league import models
from django.contrib.auth.models import User

def home(request):
    if request.method == "POST":
        race = models.Race.objects.first();
        team = models.Team.objects.get(owner=request.user, belonged_race=race)
        if request.POST.get("add")=="":
            print("ASDASDASD")
            name = request.POST.get("name")
            team.add_player(name)
        if request.POST.get("remove")=="":
            print("LLLLLLLLLLLLLLLLLLLLLL")
            name = request.POST.get("name")
            team.remove_player(name)
        return redirect("home")
    else:
        if request.user.is_authenticated:
            race = models.Race.objects.first()
            try:
                team = models.Team.objects.get(owner=request.user, belonged_race=race)
                budget=team.budget
                print(budget)
                team_players = team.selected_players.all().order_by("group", "-player__sex"); ## this returns participation objects
                players_except_team = models.Participation.objects.filter(race=race).exclude(id__in=team_players)
                return render(request, "wall.html",{"race":race,"team":team_players, "players":players_except_team, "budget": "{}".format(budget)})
            except:
                race = models.Race.objects.first()
                team = models.Team(owner=request.user, belonged_race=race)
                team.save()
                return redirect("home")
        else:
            return render(request, "home.html")


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})