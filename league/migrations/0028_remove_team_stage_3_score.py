# Generated by Django 2.0.1 on 2018-10-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0027_auto_20181012_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='stage_3_score',
        ),
    ]
