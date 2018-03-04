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


class Race(models.Model):
    name = models.CharField(max_length=255)
    # teams = models.ManyToManyField(Team)
    players = models.ManyToManyField(Player, through="Participation", related_name="races")
    created_at = models.DateTimeField(auto_now=True)

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
    finish_time = models.DurationField(default = timedelta(seconds=0))
    score = models.PositiveSmallIntegerField(default=0)
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
    selected_players = models.ManyToManyField(Participation)
    created_at = models.DateTimeField(auto_now=True)
    budget = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.owner.username+"'s Team for "+self.belonged_race.name
