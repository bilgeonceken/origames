# Generated by Django 2.0.1 on 2018-03-04 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0012_auto_20180304_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('distance', models.CharField(choices=[('Sprint', 'Sprint'), ('Middle', 'Middle'), ('Long', 'Long')], default='Middle', max_length=1)),
                ('E21E_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K21E_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('E21A_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K21A_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('E21B_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K21B_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('E20A_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K20A_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('E20B_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K20B_win_time', models.DurationField(default=datetime.timedelta(0))),
                ('K55_win_time', models.DurationField(default=datetime.timedelta(0))),
            ],
        ),
        migrations.RenameField(
            model_name='participation',
            old_name='finish_time',
            new_name='finish_time_1',
        ),
        migrations.RenameField(
            model_name='participation',
            old_name='score',
            new_name='score_1',
        ),
        migrations.RemoveField(
            model_name='race',
            name='E20A_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='E20B_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='E21A_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='E21B_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='E21E_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K20A_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K20B_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K21A_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K21B_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K21E_win_time',
        ),
        migrations.RemoveField(
            model_name='race',
            name='K55_win_time',
        ),
        migrations.AddField(
            model_name='participation',
            name='finish_time_2',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='participation',
            name='score_2',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
