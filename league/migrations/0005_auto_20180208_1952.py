# Generated by Django 2.0.1 on 2018-02-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_auto_20180208_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='players',
            field=models.ManyToManyField(related_name='races', through='league.Participation', to='league.Player'),
        ),
    ]
