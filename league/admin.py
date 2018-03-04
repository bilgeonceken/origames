from django.contrib import admin

# Register your models here.

from . import models


########### because of through field
class ParticipationInline(admin.TabularInline):
    model = models.Participation

class StageInline(admin.TabularInline):
    model = models.Race.stages.through

#######
class PlayerAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline,)

class RaceAdmin(admin.ModelAdmin):
    inlines = (ParticipationInline, StageInline)
    exclude = ('stages',)

###
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Race, RaceAdmin)
############

admin.site.register(models.Team)
admin.site.register(models.Stage)
