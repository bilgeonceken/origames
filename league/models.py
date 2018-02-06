from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    ## CHOICE CONSTANTS
    ELITE_MAN = "E21E"
    ELITE_WOMAN = "K21E"
    EXP_MAN_A = "E21A"
    EXP_WOMAN_A = "K21A"
    EXP_MAN_B = "E21B"
    EXP_WOMAN_B = "K21B"
    YOUNG_MAN_B = "E20B"
    YOUNG_WOMAN_B = "K20B"
    OLD_WOMAN = "K55"

    MALE = "M"
    FEMALE = "F"

    GROUP_1 = "1"
    GROUP_2 = "2"
    GROUP_3 = "3"


    CATEGORY_CHOICES = (
        (ELITE_MAN , "E21E"),
        (ELITE_WOMAN , "K21E"),
        (EXP_MAN_A , "E21A"),
        (EXP_WOMAN_A , "K21A"),
        (EXP_MAN_B , "E21B"),
        (EXP_WOMAN_B , "K21B"),
        (YOUNG_MAN_B , "E20B"),
        (YOUNG_WOMAN_B , "K20B"),
        (OLD_WOMAN , "K55"),
    )

    SEX_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    GROUP_CHOICES = (
        (GROUP_1, "1"),
        (GROUP_2, "2"),
        (GROUP_3, "3"),
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
    group = models.CharField(
        max_length=1,
        choices=GROUP_CHOICES,
        default=GROUP_1
    )

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["group"]


class Race(models.Model):
    name = models.CharField(max_length=255)
    # teams = models.ManyToManyField(Team)
    players = models.ManyToManyField(Player, through="Participation")


class Participation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField(default=0)


class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    belonged_race = models.ForeignKey(Race, on_delete=models.CASCADE)
    selected_players = models.ManyToManyField(Participation)
