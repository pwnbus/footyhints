# Generated by Django 3.1.1 on 2020-11-28 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_day', models.IntegerField()),
                ('start_time', models.IntegerField()),
                ('interest_score', models.FloatField(null=True)),
                ('interest_level', models.CharField(max_length=30, null=True)),
                ('attributes', models.ManyToManyField(to='web.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreModification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('games', models.ManyToManyField(to='web.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team_games', to='web.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team_games', to='web.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='score_modifications',
            field=models.ManyToManyField(to='web.ScoreModification'),
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('last_updated', models.IntegerField(null=True)),
                ('games', models.ManyToManyField(to='web.Game')),
                ('teams', models.ManyToManyField(to='web.Team')),
            ],
        ),
    ]
