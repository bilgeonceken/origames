# Generated by Django 2.0.2 on 2018-10-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0026_remove_team_joker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='official_category',
            field=models.CharField(choices=[('E21E', 'E21E'), ('K21E', 'K21E'), ('E21A', 'E21A'), ('K21A', 'K21A'), ('E21B', 'E21B'), ('K21B', 'K21B'), ('K20A', 'K20A'), ('E20B', 'E20B'), ('K20B', 'K20B'), ('K55', 'K55'), ('E20A', 'E20A')], default='E21E', max_length=4),
        ),
    ]
