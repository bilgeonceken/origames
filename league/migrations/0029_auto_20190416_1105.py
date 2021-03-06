# Generated by Django 2.0.2 on 2019-04-16 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0028_remove_team_stage_3_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='finish_time_3',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='participation',
            name='score_3',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='stage_3_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
