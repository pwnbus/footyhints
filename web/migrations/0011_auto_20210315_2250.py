# Generated by Django 3.1.1 on 2021-03-15 22:50

from django.db import migrations, models
import web.logo_storage


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20210304_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='logo_image',
            field=models.ImageField(default='web/static/images/default_competition_logo.png', storage=web.logo_storage.LogoStorage(), upload_to='web/static/images/dynamic/competitions'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo_image',
            field=models.ImageField(default='web/static/images/default_team_logo.png', storage=web.logo_storage.LogoStorage(), upload_to='web/static/images/dynamic/teams'),
        ),
    ]
