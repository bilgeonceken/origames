# Generated by Django 2.0.2 on 2018-03-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0020_stage_disqualification_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='total_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
