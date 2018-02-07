from django.forms import ModelForm, ChoiceField
from . import models

from .models import Player

class PlayerForm(ModelForm):

    class Meta:
        model = models.Player
        fields = ["name","sex", "official_category"]
