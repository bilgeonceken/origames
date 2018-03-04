from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class Player(models.Model):
    ## CHOICE CONSTANTS
    ELITE_MAN = "E21E"
    ELITE_WOMAN = "K21E"
    EXP_MAN_A = "E21A"
    EXP_WOMAN_A = "K21A"
    EXP_MAN_B = "E21B"
    EXP_WOMAN_B = "K21B"
    YOUNG_MAN_A = "E20A"
    YOUNG_WOMAN_A = "K20A"
    YOUNG_MAN_B = "E20B"
    YOUNG_WOMAN_B = "K20B"
    OLD_WOMAN = "K55"

    MALE = "M"
    FEMALE = "F"


    CATEGORY_CHOICES = (
        (ELITE_MAN , "E21E"),
        (ELITE_WOMAN , "K21E"),
        (EXP_MAN_A , "E21A"),
        (EXP_WOMAN_A , "K21A"),
        (EXP_MAN_B , "E21B"),
        (EXP_WOMAN_B , "K21B"),
        (YOUNG_WOMAN_A , "K20A"),
        (YOUNG_MAN_B , "E20B"),
        (YOUNG_WOMAN_B , "K20B"),
        (OLD_WOMAN , "K55"),
    )

    SEX_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )


    name = models.CharField(max_length=255)
    ## Usage example on views:
    ## elite_man_players = Player.objects.filter(official_category=Player.ELITE_MAN)
    sex = models.CharField(
    max_length=2,
    choices=SEX_CHOICES,
    default=MALE
    )
    official_category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default="E21E",
    )

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["name"]


class Stage(models.Model):
    SPRINT = "Sprint"
    MIDDLE = "Middle"
    LONG = "Long"

    DISTANCE_CHOICES = (
        (SPRINT, "Sprint"),
        (MIDDLE, "Middle"),
        (LONG, "Long"),
    )

    order = models.PositiveSmallIntegerField(default=0) ## day 1, day 2 etc.
    distance = models.CharField(
            max_length=6,
            choices=DISTANCE_CHOICES,
            default=MIDDLE
           )
    ## durationfield stores timedelta objects
    E21E_win_time = models.DurationField(default = timedelta(seconds=0))
    K21E_win_time = models.DurationField(default = timedelta(seconds=0))
    E21A_win_time = models.DurationField(default = timedelta(seconds=0))
    K21A_win_time = models.DurationField(default = timedelta(seconds=0))
    E21B_win_time = models.DurationField(default = timedelta(seconds=0))
    K21B_win_time = models.DurationField(default = timedelta(seconds=0))
    E20A_win_time = models.DurationField(default = timedelta(seconds=0))
    K20A_win_time = models.DurationField(default = timedelta(seconds=0))
    E20B_win_time = models.DurationField(default = timedelta(seconds=0))
    K20B_win_time = models.DurationField(default = timedelta(seconds=0))
    K55_win_time  = models.DurationField(default = timedelta(seconds=0))

    ##I'll try to reach finish time by querying by category names
    wintimes = {
    "E21E": E21E_win_time,
    "K21E": K21E_win_time,
    "E21A": E21A_win_time,
    "K21A": K21A_win_time,
    "E21B": E21B_win_time,
    "K21B": K21B_win_time,
    "E20A": E20A_win_time,
    "K20A": K20A_win_time,
    "E20B": E20B_win_time,
    "K20B": K20B_win_time,
    "K55": K55_win_time
    }


class Race(models.Model):
    name = models.CharField(max_length=255)
    # teams = models.ManyToManyField(Team)
    players = models.ManyToManyField(Player, through="Participation", related_name="races")
    created_at = models.DateTimeField(auto_now=True)
    stages = models.ManyToManyField(Stage)

    # E21E_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K21E_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # E21A_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K21A_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # E21B_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K21B_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # E20A_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K20A_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # E20B_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K20B_win_time_1 = models.DurationField(default = timedelta(seconds=0))
    # K55_win_time_1  = models.DurationField(default = timedelta(seconds=0))
    #
    # E21E_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K21E_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # E21A_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K21A_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # E21B_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K21B_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # E20A_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K20A_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # E20B_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K20B_win_time_2 = models.DurationField(default = timedelta(seconds=0))
    # K55_win_time_2  = models.DurationField(default = timedelta(seconds=0))

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["-created_at"]


class Participation(models.Model):
    GROUP_1 = "1"
    GROUP_2 = "2"
    GROUP_3 = "3"

    GROUP_CHOICES = (
        (GROUP_1, "1"),
        (GROUP_2, "2"),
        (GROUP_3, "3"),
    )


    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    finish_time_1 = models.DurationField(default = timedelta(seconds=0))
    score_1 = models.PositiveSmallIntegerField(default=0)
    finish_time_2 = models.DurationField(default = timedelta(seconds=0))
    score_2 = models.PositiveSmallIntegerField(default=0)
    group = models.CharField(
        max_length=1,
        choices=GROUP_CHOICES,
        default=GROUP_1
    )

    def __str__(self):
        return self.player.name+" Participation"



class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    belonged_race = models.ForeignKey(Race, on_delete=models.CASCADE)
    selected_players = models.ManyToManyField(Participation, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    budget = models.PositiveSmallIntegerField(default=100)


    def add_player(self, playername):
        race = Race.objects.first()
        player = Participation.objects.filter(race=race, player__name=playername)[0]

        group_counts = {
        "1":0,
        "2":0,
        "3":0
        }

        group_limits = {
        "1":3,
        "2":4,
        "3":2
        }
        for p in self.selected_players.all():
            group_counts[p.group]+=1

        if group_counts[player.group] >= group_limits[player.group]:
            print("Can't add more of the same group")
            return
        if self.budget >= player.price:
            self.selected_players.add(player)
            self.budget -= player.price
            self.save()
        else:
            print("Not enough budget")

    def remove_player(self, playername):
        race = Race.objects.first()
        player = Participation.objects.get(race=race, player__name=playername)
        try:
            self.selected_players.remove(player)
        except:
            return
        finally:
            self.budget += player.price
            self.save()
    def __str__(self):
        return self.owner.username+"'s Team for "+self.belonged_race.name
