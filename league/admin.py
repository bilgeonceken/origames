from django.contrib import admin

# Register your models here.

from . import models


########### because of through field
class ParticipationInline(admin.TabularInline):
    model = models.Participation

class PlayerAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

class RaceAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Race, RaceAdmin)
############

admin.site.register(models.Team)
