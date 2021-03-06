# Generated by Django 3.1.1 on 2021-02-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210215_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='team',
            name='logo',
        ),
        migrations.AddField(
            model_name='competition',
            name='logo_image',
            field=models.ImageField(null=True, upload_to='web/static/images/competitions', verbose_name='img'),
        ),
        migrations.AddField(
            model_name='team',
            name='logo_image',
            field=models.ImageField(null=True, upload_to='web/static/images/teams', verbose_name='img'),
        ),
    ]
