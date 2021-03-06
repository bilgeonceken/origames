# Generated by Django 2.0.2 on 2018-04-04 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0022_race_is_active'),
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
        migrations.AlterField(
            model_name='participation',
            name='group',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.PositiveSmallIntegerField(default=90),
        ),
    ]
