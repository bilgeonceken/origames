# Generated by Django 2.0.1 on 2018-10-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0024_auto_20181010_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='joker',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]