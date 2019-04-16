from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver


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

    CATEGORY_CHOICES = ((ELITE_MAN, "E21E"), (ELITE_WOMAN, "K21E"),
                        (EXP_MAN_A, "E21A"), (EXP_WOMAN_A, "K21A"), (EXP_MAN_B,
                                                                     "E21B"),
                        (EXP_WOMAN_B, "K21B"), (YOUNG_WOMAN_A,
                                                "K20A"), (YOUNG_MAN_B, "E20B"),
                        (YOUNG_WOMAN_B,
                         "K20B"), (OLD_WOMAN, "K55"), (YOUNG_MAN_A, "E20A"))

    SEX_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    name = models.CharField(max_length=255)
    ## Usage example on views:
    ## elite_man_players = Player.objects.filter(official_category=Player.ELITE_MAN)
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)
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

    order = models.PositiveSmallIntegerField(default=0)  ## day 1, day 2 etc.
    distance = models.CharField(
        max_length=6, choices=DISTANCE_CHOICES, default=MIDDLE)

    disqualification_time = models.DurationField(default=timedelta(seconds=0))

    ## durationfield stores timedelta objects
    E21E_win_time = models.DurationField(default=timedelta(seconds=0))
    K21E_win_time = models.DurationField(default=timedelta(seconds=0))
    E21A_win_time = models.DurationField(default=timedelta(seconds=0))
    K21A_win_time = models.DurationField(default=timedelta(seconds=0))
    E21B_win_time = models.DurationField(default=timedelta(seconds=0))
    K21B_win_time = models.DurationField(default=timedelta(seconds=0))
    E20A_win_time = models.DurationField(default=timedelta(seconds=0))
    K20A_win_time = models.DurationField(default=timedelta(seconds=0))
    E20B_win_time = models.DurationField(default=timedelta(seconds=0))
    K20B_win_time = models.DurationField(default=timedelta(seconds=0))
    K55_win_time = models.DurationField(default=timedelta(seconds=0))


class Race(models.Model):
    name = models.CharField(max_length=255)
    # teams = models.ManyToManyField(Team)
    players = models.ManyToManyField(
        Player, through="Participation", related_name="races")
    created_at = models.DateTimeField(auto_now=True)
    stages = models.ManyToManyField(Stage)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Participation(models.Model):
    GROUP_1 = "1"
    GROUP_2 = "2"

    GROUP_CHOICES = (
        (GROUP_1, "1"),
        (GROUP_2, "2"),
    )

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    finish_time_1 = models.DurationField(default=timedelta(seconds=0))
    score_1 = models.PositiveSmallIntegerField(default=0)
    finish_time_2 = models.DurationField(default=timedelta(seconds=0))
    score_2 = models.PositiveSmallIntegerField(default=0)
    finish_time_3 = models.DurationField(default=timedelta(seconds=0))
    score_3 = models.PositiveSmallIntegerField(default=0)
    total_score = models.PositiveSmallIntegerField(default=0)
    group = models.CharField(
        max_length=1, choices=GROUP_CHOICES, default=GROUP_1)

    def __str__(self):
        return self.player.name + " Participation"


@receiver(pre_save, sender=Participation)
def update_participation_score(sender, instance, *args, **kwargs):
    if instance.finish_time_1.total_seconds() != 0:
        stage1 = instance.race.stages.all().get(order="1")
        ##this returns a dic with relevant fields of like:
        ## there are two stages of the race os 0 is the first one
        ## {'id': 3, 'order': 1, 'distance': 'Middle', 'E21E_win_time': datetime.timedelta(0), 'K21E_win_time': datetime.timedelta(0), 'E21A_win_time': datetime.timedelta(0), 'K21A_win_time': datetime.timedelta(0), 'E21B_win_time': datetime.timedelta(0), 'K21B_win_time': datetime.timedelta(0), 'E20A_win_time': datetime.timedelta(0), 'K20A_win_time': datetime.timedelta(0), 'E20B_win_time': datetime.timedelta(0), 'K20B_win_time': datetime.timedelta(0), 'K55_win_time': datetime.timedelta(0)}
        stage1_fields_dict = instance.race.stages.values()[0]
        ## now i can get related finish time concataneting participation object's
        ## category and the string "_win_time"
        disqualification_time = stage1_fields_dict["disqualification_time"]
        disqualification_time_seconds = disqualification_time.total_seconds()
        wintime1 = stage1_fields_dict[instance.player.official_category +
                                      "_win_time"]
        ## i need seconds to calculate easily
        wintime1seconds = wintime1.total_seconds()
        finish_time_1seconds = instance.finish_time_1.total_seconds()
        if finish_time_1seconds <= disqualification_time_seconds:
            ## official score
            instance.score_1 = (wintime1seconds / finish_time_1seconds) * 1000
        else:
            instance.score_1 = 0
    if instance.finish_time_2.total_seconds() != 0:
        stage2 = instance.race.stages.all().get(order="2")
        stage2_fields_dict = instance.race.stages.values()[1]
        disqualification_time = stage2_fields_dict["disqualification_time"]
        disqualification_time_seconds = disqualification_time.total_seconds()
        wintime2 = stage2_fields_dict[instance.player.official_category +
                                      "_win_time"]
        wintime2seconds = wintime2.total_seconds()
        finish_time_2seconds = instance.finish_time_2.total_seconds()
        if finish_time_2seconds <= disqualification_time_seconds:
            instance.score_2 = (wintime2seconds / finish_time_2seconds) * 1000
        else:
            instance.score_2 = 0
    if instance.finish_time_3.total_seconds() != 0:
        stage3 = instance.race.stages.all().get(order="3")
        stage3_fields_dict = instance.race.stages.values()[2]
        disqualification_time = stage3_fields_dict["disqualification_time"]
        disqualification_time_seconds = disqualification_time.total_seconds()
        wintime3 = stage3_fields_dict[instance.player.official_category +
                                      "_win_time"]
        wintime3seconds = wintime3.total_seconds()
        finish_time_3seconds = instance.finish_time_3.total_seconds()
        if finish_time_3seconds <= disqualification_time_seconds:
            instance.score_3 = (wintime3seconds / finish_time_3seconds) * 1000
        else:
            instance.score_2 = 0

    instance.total_score = instance.score_1 + instance.score_2


class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    belonged_race = models.ForeignKey(Race, on_delete=models.CASCADE)
    selected_players = models.ManyToManyField(Participation, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    budget = models.PositiveSmallIntegerField(default=100)
    stage_1_score = models.PositiveSmallIntegerField(default=0)
    stage_2_score = models.PositiveSmallIntegerField(default=0)
    stage_3_score = models.PositiveSmallIntegerField(default=0)
    total_score = models.PositiveSmallIntegerField(default=0)

    def add_player(
            self,
            playername,
    ):
        race = Race.objects.first()
        player = Participation.objects.filter(
            race=race, player__name=playername)[0]

        group_counts = {
            "1": 0,
            "2": 0,
        }

        group_limits = {
            "1": 4,
            "2": 5,
        }

        ## get group counts to check if the group is full or not later
        for p in self.selected_players.all():
            group_counts[p.group] += 1


        if group_counts[player.group] >= group_limits[player.group]:
            return 1

        # messages.add_message(request, messages.error, "Can't add more of the same group")
        if self.budget >= player.price:
            self.selected_players.add(player)
            self.budget -= player.price
            self.save()
            return 0
            # messages.add_message(request, messages.success, "Added "+player.player.name+"successfully!")
        else:
            return 2
            # raise Exception("Not enough money")
            # messages.add_message(request, messages.error, "Not enough money")

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
        return self.owner.username + "'s Team for " + self.belonged_race.name


@receiver(post_save, sender=Participation)
def update_team_score(sender, instance, *args, **kwargs):
    for team in instance.team_set.all():
        team.stage_1_score = 0
        team.stage_2_score = 0
        team.stage_3_score = 0
        team.total_score = 0
        for player in team.selected_players.all():
            team.stage_1_score += player.score_1
            team.stage_2_score += player.score_2
            team.stage_3_score += player.score_3
            team.total_score += player.total_score
        team.save()
