# Generated by Django 2.0.1 on 2018-03-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0016_auto_20180304_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='distance',
            field=models.CharField(choices=[('Sprint', 'Sprint'), ('Middle', 'Middle'), ('Long', 'Long')], default='Middle', max_length=6),
        ),
    ]
