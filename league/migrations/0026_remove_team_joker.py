# Generated by Django 2.0.1 on 2018-10-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0025_auto_20181011_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='joker',
        ),
    ]