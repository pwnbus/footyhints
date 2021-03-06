# Generated by Django 3.1.1 on 2021-03-04 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_team_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='draws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goal_difference',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_against',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_for',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='loses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
