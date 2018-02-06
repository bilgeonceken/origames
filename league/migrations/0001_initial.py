# Generated by Django 2.0.1 on 2018-02-06 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField()),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('official_category', models.CharField(choices=[('E21E', 'E21E'), ('K21E', 'K21E'), ('E21A', 'E21A'), ('K21A', 'K21A'), ('E21B', 'E21B'), ('K21B', 'K21B'), ('E20B', 'E20B'), ('K20B', 'K20B'), ('K55', 'K55')], default='E21E', max_length=4)),
                ('group', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=1)),
            ],
            options={
                'ordering': ['group'],
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('players', models.ManyToManyField(through='league.Participation', to='league.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belonged_race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Race')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('selected_players', models.ManyToManyField(to='league.Participation')),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Player'),
        ),
        migrations.AddField(
            model_name='participation',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.Race'),
        ),
    ]
